import os
import win32com.client

def main():

    # Get the absolute path to the Excel file in the same directory as the script
    script_dir = os.path.dirname(os.path.realpath(__file__))
    excel_file_path = os.path.join(script_dir, 'test.xlsx')

    o = win32com.client.Dispatch("Excel.Application")
    o.Visible = 1
    wb = o.Workbooks.Open(excel_file_path)
    ws = wb.Worksheets[1]

    # Set page setup options
    ws.PageSetup.Zoom = False
    ws.PageSetup.FitToPagesTall = False
    ws.PageSetup.FitToPagesWide = 1
    ws.PageSetup.LeftMargin = 25
    ws.PageSetup.RightMargin = 25
    ws.PageSetup.TopMargin = 50
    ws.PageSetup.BottomMargin = 50

    # Set the print area (assuming 'print_area' is defined elsewhere in your code)


    # Set PDF export options
    pdf_path = os.path.join(script_dir, 'test.pdf')
    wb.ExportAsFixedFormat(0, pdf_path)  # 0 represents PDF format

    # Close Excel
    wb.Close(False)
    o.Quit()
