import csv

header = ["Name", "Age","Address","Interest"]
row ={
    "Name":"Rajesh Kumar Tharu",
    "Age": 22,
    "Address":"Banke",
    "Interest":"Django Developer"
}

with open("csvfile.csv","w", newline = '') as file:
    writer = csv.DictWriter(file, header)
    writer.writeheader()

    writer.writerow(row)


print("In csv file header is set successfully!!!")


with open("csvfile.csv","r") as file:
    reader = csv.reader(file)
    for row in file:
        print(row)