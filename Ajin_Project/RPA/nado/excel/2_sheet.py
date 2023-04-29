from openpyxl import Workbook
wb = Workbook()
# wb.active
ws = wb.create_sheet()  # 새로운 sheet 기본이름으로 생성
ws.title = "MySheet"
ws.sheet_properties.tabColor = "ff66ff"
wb.save("sample.xlsx")
