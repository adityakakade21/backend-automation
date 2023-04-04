import csv

with open('utilities/loanapp.csv') as csvFile:
    csvReader = csv.reader(csvFile,delimiter=',')
    names = []
    statuses = []
    for row in csvReader:
        names.append(row[0])
        statuses.append(row[1])

    print(names)
    print(statuses)

with open('utilities/loanapp.csv','a') as wFile:
    csvWriter = csv.writer(wFile)
    csvWriter.writerow(["Kat","approved"])