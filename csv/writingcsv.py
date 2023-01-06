from csv import writer

with open("/home/ashish/pythonprograms/csv/fighterwrite.csv", "w") as file:
    csv_writer = writer(file)
    csv_writer.writerow(["Character", "Move"])
    csv_writer.writerow(["Ryu", "Hadouken"])
    