import csv
import base64
import os

from PIL import Image # type: ignore

# Insert your own desired file and filepath 
Dirpath = r"C:\Users\16127\Desktop\EmployeeID"
Files = os.listdir(Dirpath)

for File in Files:
    imgPath = os.path.join(Dirpath, File)
    with open(''+ imgPath + '', "rb") as f:
        encoded_image = base64.b64encode(f.read())
    print(encoded_image)