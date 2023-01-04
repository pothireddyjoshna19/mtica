def PrintMon():
    print("Monday")
def printTue():
    print("Tuesday")
def printWed():
    print("Wednesday")
def printThu():
    print("Thursday")
def printFri():
    print("Friday")
def printSat():
    print("Saturday")
def printSun():
    print("Sunday")
def choice():
    print("Enter day number between 1-7")
dayDict={1:PrintMon,2:printTue,3:printWed,4:printThu,5:printFri,6:printSat,7:printSun}
choice()
dayNo=int(input())
if dayNo>=1 and dayNo<=7:
    dayDict[dayNo]()
else:
     print("INVALID")
    
    
      
