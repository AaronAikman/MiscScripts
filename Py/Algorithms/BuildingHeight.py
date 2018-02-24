# CalculateBuildingHeight.py
# Aaron Aikman
# Calculate height of a building based upon the inputted number of floors

while True:
    numFloors = input("Enter a number of floors (returns cm):")
    if (numFloors == ""):
        break
    buildingHeight = ((3.1 * numFloors) + 7.75 + (1.55 * (numFloors / 30)))
    print buildingHeight * 100
    print "\n"
