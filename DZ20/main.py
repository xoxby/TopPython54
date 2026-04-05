import re


password = "my-p@ssw0rd"
password_pattern = r"^[A-Za-z0-9_@-]{6,18}$"

print(re.findall(password_pattern, password))


text = "В июне 2021 года, 02/06/2021, 05/06/2021, 14/06/2021, были зафиксированы максимумы ежемесячных осадков."
date_pattern = r"\b\d{2}/\d{2}/\d{4}\b"

print(re.findall(date_pattern, text))
