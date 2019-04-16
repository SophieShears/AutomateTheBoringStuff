# python3.6
# excelToCsv.py - Converts all excel files in a directory to csv

import os, csv, openpyxl

os.chdir(r'E:\Scripts\Automate\excelConvert')

for excelFile in os.listdir('.'):
    # Skip non-xlsx files, load the workbook object.
    if not excelFile.endswith('.xlsx'):
        continue
    wb = openpyxl.load_workbook(os.path.basename(excelFile))

    for sheetName in wb.get_sheet_names():
        # Loop through every sheet in the workbook.
        sheet = wb.get_sheet_by_name(sheetName)

        # Create the CSV filename from the Excel filename and sheet title.
        filename = str(os.path.basename(excelFile) + '_' + sheetName + '.csv')

        # Create the csv.writer object for this CSV file.
        csvFile = open(filename, 'w', newline='')
        csvWriter = csv.writer(csvFile)

        # Loop through every row in the sheet.
        for rowNum in range(1, sheet.max_row + 1):
            rowData = []    # append each cell to this list
            # Loop through each cell in the row.
            for colNum in range(1, sheet.max_column + 1):
                # Append each cell's data to rowData.
                rowData.append(sheet.cell(row=rowNum, column=colNum).value)

            # Write the rowData list to the CSV file.
            csvWriter.writerow(rowData)
        csvFile.close()
