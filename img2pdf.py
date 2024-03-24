# GPT 생성코드

from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os


def save_images_as_pdf(image_folder, pdf_file_name):
    # 폴더 내의 모든 파일 리스트 가져오기
    files = [
        f
        for f in os.listdir(image_folder)
        if f.lower().endswith((".png", ".jpg", ".jpeg"))
    ]
    files.sort()  # 이름 순으로 정렬, 필요한 경우 다른 정렬 방법을 사용

    # 첫 번째 이미지를 열어 PDF 크기 설정
    first_image_path = os.path.join(image_folder, files[0])
    first_image = Image.open(first_image_path)
    pdf_width, pdf_height = first_image.size

    # PDF 생성
    c = canvas.Canvas(pdf_file_name, pagesize=(pdf_width, pdf_height))

    for f in files:
        image_path = os.path.join(image_folder, f)
        try:
            # 이미지 파일 열기
            image = Image.open(image_path)

            # 이미지를 PDF에 추가
            c.drawImage(image_path, 0, 0, width=pdf_width, height=pdf_height)
            c.showPage()
        except Exception as e:
            print(f"An error occurred while processing the image {image_path}: {e}")

    c.save()
    print(f"PDF saved as {pdf_file_name}")


# 이미지가 저장된 폴더 경로
image_folder = r"C:\Users\Jang\Desktop\school\shop\temp"

# PDF 파일 이름
pdf_file_name = r"C:\Users\Jang\Desktop\output.pdf"


# 함수 호출
save_images_as_pdf(image_folder, pdf_file_name)
