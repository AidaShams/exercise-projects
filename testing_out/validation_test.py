import re
email = "aidashmas77@gmail.com"
print(re.match(r"^[a-zA-Z0-9]\w+@(gmail|yahoo).com$",email))