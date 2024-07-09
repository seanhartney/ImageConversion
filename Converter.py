import csv
import base64
import os
#with open("9hm6q.jpeg", "rb") as f:

directory = 'C:\Users\16127\StOlafCode\SeanCode\ImageConversion'

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        print(f)
