from http.server import HTTPServer
import re
from turtle import title



############################# EXTRACTING DATA FROM TEXT FILE AND WRITE TO NEW TEXT FILE  ###############################
file = open("bear.txt")
content = file.read()
file.close()
with open("first.txt", "w") as first:
    first.write(content[:90])
