def printBlue():
    print('you choose blue!\n')
    return
def printRed():
    print('you choose red!\n')
    return
def printGreen():
    print('you choose green!\n')
    return
def printPink():
    print('you choose pink!\n')
    return
def choice():
    print("0:Blue")
    print("1:Red")
    print("2:Green")
    print("3:Pink")
    print("4:Quit")
    return
colorselect={0:printBlue,1:printRed,2:printGreen,3:printPink}
selection=0
while True:
    if selection == 4:break
    choice()
    selection=int(input("select a color option:"))
    if(selection>=0) and (selection<4):
        colorselect[selection]()
