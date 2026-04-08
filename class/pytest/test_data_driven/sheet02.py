import openpyxl
def get_test_data():
    wb=openpyxl.load_workbook("sample.xlsx")
    ws= wb("Sheet1")
    data=[]
    for row in ws.iter_rows(min_row=2, values_only=True):
        data.append(row)
    return data


