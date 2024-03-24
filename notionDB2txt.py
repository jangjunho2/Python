import requests, os


# 실행에 필요한 정보 읽기 (메시지 양식, 데이터베이스주소, 토큰), 폴더 생성
def setup_environment():
    with open("./msg.txt", "r", encoding="utf-8") as f:
        message_template = f.read()

    with open("./url.txt", "r", encoding="utf-8") as f:
        database_url = f.read()

    with open("./secret.txt", "r", encoding="utf-8") as f:
        secret = f.read()

    # msg 폴더 없을시 생성
    directory_path = f"./msg"
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    return message_template, database_url, secret


# 데이터 베이스 ID 추출
def extract_db_id(notion_url: str) -> str:
    parts = notion_url.split("/")
    last_part = parts[-1]
    return last_part.split("?")[0]


# 메시지 양식 전처리 작업
def preprocess(message_template: str) -> str:
    # {W*} -> {Classes[W*]}
    while "{W" in message_template:
        start_index = message_template.find("{W")
        if start_index != -1:
            end_index = message_template.find("}", start_index)
            substring = message_template[start_index : end_index + 1]
            new_string = list(substring)
            new_string[0] = "["
            new_string[-1] = "]"
            new_string = "".join(new_string)
            new_string = "{Classes" + new_string + "}"
            # print(new_string)
        message_template = message_template.replace(substring, new_string)

    # {HW*} -> {Assignment[HW*]}
    while "{H" in message_template:
        start_index = message_template.find("{H")
        if start_index != -1:
            end_index = message_template.find("}", start_index)
            substring = message_template[start_index : end_index + 1]
            new_string = list(substring)
            new_string[0] = "["
            new_string[-1] = "]"
            new_string = "".join(new_string)
            new_string = "{Assignments" + new_string + "}"
            # print(new_string)
            message_template = message_template.replace(substring, new_string)

    # {Test*} -> {Exams[Test*]}
    while "{T" in message_template:
        start_index = message_template.find("{T")
        if start_index != -1:
            end_index = message_template.find("}", start_index)
            substring = message_template[start_index : end_index + 1]
            new_string = list(substring)
            new_string[0] = "["
            new_string[-1] = "]"
            new_string = "".join(new_string)
            new_string = "{Exams" + new_string + "}"
            # print(new_string)
            message_template = message_template.replace(substring, new_string)
    return message_template


# 데이터베이스에서 데이터 읽어오기


def query_notion_database() -> dict:
    # 데이터베이스 쿼리를 위한 URL과 헤더 설정
    url = f"https://api.notion.com/v1/databases/{database}/query"
    headers = {
        "Authorization": f"Bearer {secret}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28",
    }

    response = requests.post(url, headers=headers)
    data = response.json()

    return data


# 학생 정보 추출
def extract_and_store_student_info(data: dict) -> list:
    # 학생 정보를 담을 리스트
    students = []

    # 응답 데이터에서 필요한 속성 정보 추출
    for item in data.get("results", []):
        properties = item.get("properties", {})

        # '이름' 속성에서 이름 추출
        name = properties.get("이름", {}).get("title", [])
        name_text = name[0].get("text", {}).get("content", "") if name else ""

        # 이름이 비어있으면 이 학생은 스킵
        if not name_text:
            continue

        # 이름이 있을 경우 나머지 정보 처리
        student_info = {
            "학생이름": name_text,
            "출석": False,
            "연락처(본인)": "",
            "연락처(부모님)": "",
            "Exams": {},
            "Assignments": {},
            "Classes": {},
            "학교": "",
        }
        for (
            prop_name,
            prop_val,
        ) in properties.items():  # O,X 등 수정할시 Notion 먼저 체크 할 것!

            # property : text
            if prop_name == "이름":
                student_info["학생이름"] = (
                    prop_val.get("title", [{}])[0].get("text", {}).get("content", "")
                )

            elif prop_name == "출석":
                student_info["출석"] = "O" if prop_val.get("checkbox", False) else "X"

            # property : rich_text or number?
            elif prop_name.startswith(
                "Test"
            ):  # TEST 값이 있으면 제출 , 값이 없으면 미제출
                # student_info["Exams"][prop_name] =  prop_val.get("rich_text") if prop_val.get("rich_text", False) else "데이터 X" # 값이 1개 일경우 사용 가능 속성 rich_text

                # 값이 있는 경우
                if prop_val.get("rich_text"):
                    first_rich_text = prop_val.get("rich_text")[0]
                    text_content = first_rich_text.get("text", {}).get("content", "")

                    # ,
                    if text_content == ",":
                        text_content = "미제출 / 미제출"
                    # *,*
                    elif text_content[0].isdigit() and text_content[-1].isdigit():
                        text_content = "제출 / 제출"
                    # ,*    or    *,
                    else:
                        if text_content[0].isdigit():
                            text_content = "제출 / 미제출"
                        else:
                            text_content = "미제출 / 제출"

                    student_info["Exams"][prop_name] = text_content
                # 값이 없는 경우
                else:
                    student_info["Exams"][prop_name] = "None"

            elif prop_name.startswith("HW"):
                student_info["Assignments"][prop_name] = (
                    prop_val.get("number")
                    if prop_val.get("number") is not None
                    else "미제출"
                )

            # property : 체크박스
            elif prop_name.startswith("W"):
                student_info["Classes"][prop_name] = (
                    "O" if prop_val.get("checkbox", False) else "X"
                )

            # property : phone_number
            elif prop_name == "연락처(본인)":
                student_info["연락처(본인)"] = prop_val.get("phone_number", "")

            elif prop_name == "연락처(부모님)":
                student_info["연락처(부모님)"] = prop_val.get("phone_number", "")

            # property : multi_select
            elif prop_name == "학교":
                multi_select_values = prop_val.get("multi_select", [])
                # 모든 선택된 항목의 이름을 쉼표로 구분하여 결합
                student_info["학교"] = ", ".join(
                    [item.get("name", "") for item in multi_select_values]
                )

        students.append(student_info)
    return students


def create_message(students: list, message_template: str, print_student_info=False):
    for s in students:
        if print_student_info:
            print(s)  # 학생 정보 출력
            print("\n")

        # 학교 폴더 없을시 생성
        directory_path = f'./msg/{s["학교"]}'
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)

        # 개인 메시지 생성
        message = message_template.format(**s)
        with open(
            f'./msg/{s["학교"]}/{s["학생이름"]}.txt', "w", encoding="utf-8"
        ) as file:
            file.write(message)

    print(
        "------------------------------   메시지 생성 완료     ------------------------------"
    )


########################################################################################################################################################################
########################################################################################################################################################################
########################################################################################################################################################################
########################################################################################################################################################################

message_template, database_url, secret = setup_environment()
database = extract_db_id(database_url)
message_template = preprocess(message_template)  # 전처리 과정
print(message_template)
data = query_notion_database()
# print(data)
students = extract_and_store_student_info(data)
create_message(students, message_template)
