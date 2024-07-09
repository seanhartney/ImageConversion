import csv
import base64
import os

from PIL import Image # type: ignore

# Insert your own desired file and filepath 
Dirpath = r"C:\Users\16127\Desktop\EmployeeID"
Files = os.listdir(Dirpath)

# Creating CSV file 
fields = ['Employee ID', 'Base64 Image', 'Number']

# Empty array of rows for spreadsheet
rows = []

numEmployees = 0

csvFileName = "ConvertedImages.csv"

for File in Files:
    imgPath = os.path.join(Dirpath, File)
    with open(''+ imgPath + '', "rb") as f:
        encoded_image = base64.b64encode(f.read())
        numEmployees = numEmployees + 1
        empID = File[:-5]
        tempArray = [empID, encoded_image, numEmployees]
        rows.append(tempArray)

with open(csvFileName, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)

print(numEmployees)

