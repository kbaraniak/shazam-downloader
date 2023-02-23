import csv

def csv_to_list(file):
  csvlist = []
  with open(file, 'r') as file:
    csvmixed = csv.reader(file)
    for row in csvmixed:
      x = row[1:]
      if (len(x) >= 1):
        if not(x[0] == "Artist"):
          csvlist.append(x)
    return csvlist
