import win32com.client

def launch_explorer():
    explore = win32com.client.Dispatch("InternetExplorer.Application")
    explore.visible = True
    for prop in dir(explore):
        print(prop)

def launch_word():
    word = win32com.client.Dispatch("Word.Application")
    word.visible = True

def launch_excel():
    excel = win32com.client.Dispatch("Excel.Application")
    excel.visible = True
    # wb = excel.Workbook.Add()
    # ws = wb.Worksheets("Sheet1")

if __name__ == "__main__":
    launch_explorer()
    # launch_word()
    # launch_excel()