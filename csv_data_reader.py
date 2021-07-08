import csv
from hash_table import HashTable

with open('./data/package_data.csv') as csv_file:
    hashTable = HashTable()
    csv_reader = csv.reader(csv_file, delimiter=',')
    counter=0
    for row in csv_reader:
        if len(row) == 9:
            row[8] = "At Hub"
        else:
            row.append("At Hub")
        row.append("awailible")
        row.append("")
        hashTable.add(row[0],row[1:])
        counter+=1
csv_file.close()


with open('./data/distance_name.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    locations = {}
    for row in csv_reader:
        locations[row[0]] = row[2]
    def get_location_data():
        return locations


with open('./data/distance_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    distances = []
    for row in csv_reader:
        distances.append(row)

def get_hash_table():
    return hashTable

def get_hash_size():
    return counter
def get_distance_data():
    return distances
    
def reset_hash_table():
    hashTable.table.clear()
    with open('./data/package_data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        counter=0
        for row in csv_reader:
            if len(row) == 9:
                row[8] = "At Hub"
            else:
                row.append("At Hub")
            row.append("awailible")
            row.append("")
            hashTable.add(row[0],row[1:])
            counter+=1
    csv_file.close()