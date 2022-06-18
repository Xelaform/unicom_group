import csv

#with open("file1.csv", "r", newline='', encoding="UTF-8") as f1:
#    reader1 = csv.DictReader(f1, delimiter=';')
# for row in reader1:
 #       with open("file2.csv", "r", newline='', encoding="UTF-8") as f2:
  #          reader2 = csv.DictReader(f1, delimiter=';')
#
 #           print(row['phone'], row['status'])

with open('file1.csv', 'r') as f1, open('file2.csv', 'r') as f2:
    fileone = f1.readlines()
    filetwo = f2.readlines()

for line1 in fileone:
    for line2 in filetwo:
        if line1[2] == 12 and line2[2] == 12:
            print(line1, line2)
            print("СОВПАЛО")