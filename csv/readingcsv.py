from csv import DictReader

with open("/home/ashish/pythonprograms/csv/fighter.csv") as file:
    csv_reader = DictReader(file, delimiter = "|")
    for row in csv_reader:
        print(row)


