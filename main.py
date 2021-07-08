from route import startTheDay
from csv_data_reader import get_hash_table, reset_hash_table
from package_manager import getTotalDistance

if __name__ == "__main__":
    print("Total distance traveled: ", getTotalDistance())
    inputOption = -1
    while inputOption !=0:
        print ('Enter 1 to find a single  package by ID number at a specific time',
               '\nEnter 2 to list all packages at a specific time',
               '\nEnter 0 to exit')
        inputOption = int(input('> '))
        if inputOption ==1:
            inputTime = input('Enter a time (HH:MM AM/PM): ')
            packageID = input('Enter the package ID Number: ')    
            startTheDay(inputTime)
            for obj in list(get_hash_table().table):
                if obj[0] == packageID:
                    print('Package:',obj[0],obj[1][0],obj[1][4],obj[1][1],obj[1][3],obj[1][5],obj[1][7],obj[1][9])
                    input("Press Enter to continue...")
        elif inputOption == 2:
            inputTime = input('Enter a time (HH:MM AM/PM): ')
            startTheDay(inputTime)
            for obj in list(get_hash_table().table):
                print('Package:',obj[0],obj[1][0],obj[1][4],obj[1][1],obj[1][3],obj[1][5],obj[1][7],obj[1][9])
            input("Press Enter to continue...")
        reset_hash_table()