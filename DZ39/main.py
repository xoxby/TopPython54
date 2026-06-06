import csv


data = [
    ["hostname", "vendor", "model", "location"],
    ["sw1", "Cisco", "3750", "London"],
    ["sw2", "Cisco", "3850", "Liverpool"],
    ["sw3", "Cisco", "3650", "Liverpool"],
    ["sw4", "Cisco", "3650", "London"],
]

with open("data.csv", "w") as f:
    writer = csv.writer(f, delimiter=";", lineterminator="\n")
    writer.writerows(data)

with open("data.csv") as r_file:
    file_reader = csv.reader(r_file, delimiter=";")

    for row in file_reader:
        print(row)
