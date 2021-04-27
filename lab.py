import re

string = "IF2240 tubes basis data 22/04/2021"
regex = "(\w{2}\d{4})|(tubes)|(tucil)|(\d{2}/\d{2}/\d{2})"

print(re.findall(regex, string))

txt = "The rain in Spain"
x = re.findall("^The.*Spain$", txt) 
print(x)