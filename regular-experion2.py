#Email Validation and password policy checker

import re


pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
pattern2 = re.compile(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$")


string = "javad.nemati65@gmail.com"
a = pattern.search(string)
print(a)

string2 = "Aa@123456"
passwd = pattern2.fullmatch(string2)
print(passwd)