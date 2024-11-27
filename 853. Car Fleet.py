# cars speed merge to lowest speed in fleet when position of car passes position of car in front, position change to car in back
# put if reach target at the end because car passing at finish line is still considered the same fleet.
# return number of fleets arrive at destination
# V = m / s

target = 10
position = [0,4,2]
speed = [2,1,3]

# initial ide: use float division
def carFleet(target, position, speed):
    # start off with each car being their own fleet
    fleet = len(position)

    # sort list based on position
    sortedPos = []

    for i, pos in enumerate(position):
        # calc for time taken to reach target
        timeTaken = float(target - pos) / float(speed[i])

        sortedPos.append([pos, timeTaken])
    
    # sort list based on pos
    sortedPos = sorted(sortedPos)
    print(sortedPos)
    # iterate from the 2nd closest car to target (back)
    for i in reversed(range(len(position) - 1)):
        # combine fleet if car passes another car (less time taken)
        if sortedPos[i][1] <= sortedPos[i + 1][1]:
            # change time taken to be equal to the slowest speed (currently just changed to speed of car in front)
            sortedPos[i][1] = sortedPos[i + 1][1]
            fleet -= 1
        
    return fleet

print(carFleet(target, position, speed))

# might use zip next time




