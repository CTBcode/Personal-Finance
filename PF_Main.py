import csv
#import File_Name
month = "Imported month Name"

file = f"name_{month}.scv"

transactions = []

with open(file, mode="r") as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        date = row[0]
        name = row[1]
        amount = float(row[2])
        transaction = ((date, name, amount))
        print(transaction)
        transactions.add(transaction)

#sa = File_Name.service_account()
#sh = sa.open("")