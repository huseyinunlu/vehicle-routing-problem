from datetime import *
from package_manager import *
from csv_data_reader import *

DAY_STARTING_TIME = "8:00 AM"
        

#410 S State St, Salt Lake City, UT 84111
def startTheDay(endTime,startTime = DAY_STARTING_TIME):
    currentDateTime = datetime.strptime(startTime, '%I:%M %p')
    endDateTime = datetime.strptime(endTime, '%I:%M %p')
    counter = 0
    while currentDateTime < endDateTime:
        if currentDateTime == datetime.strptime('10:20 AM', '%I:%M %p'):
            get_hash_table().getValue('9')[0:4] = '410 S State St', 'Salt Lake City', 'UT', '84111'
            thirdTruck.leavingTime = '10:20 AM'
        for trck in getTrucks():
            if trck.leavingTime != '':
                if trck.startedToRoute == False and datetime.strptime(trck.leavingTime, '%I:%M %p') <= currentDateTime:
                    trck.startedToRoute = True
                    trck.nextPackage = getDistance('0', getlocationIndex(trck.locations[trck.visitedPoints]))
                    for i in trck.packagesKeys:
                        get_hash_table().getValue(str(i))[7] = 'En Routing'
            if trck.startedToRoute and trck.isFinished == False:
                trck.travelledDistance += 18/60
                if  trck.lengthOfRoute() > trck.travelledDistance:
                    for index in range(len(trck.packagesKeys)):
                        if get_hash_table().getValue(trck.packagesKeys[index])[7] == "En Routing":
                            if trck.getDistanceFromStart(index) <= trck.travelledDistance+18/60:
                                counter +=1
                                get_hash_table().getValue(trck.packagesKeys[index])[7] = 'Delivered'
                                get_hash_table().getValue(trck.packagesKeys[index])[9] = currentDateTime.strftime('%I:%M %p')
                elif trck.isFinished == False:
                    trck.isFinished = True
        currentDateTime += timedelta(minutes=1)

    
