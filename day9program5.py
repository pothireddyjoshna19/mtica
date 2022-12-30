def printMonth(dn):
    if(dn==1):
        return 'january'
    elif(dn==2):
        return 'febrauary'
    elif(dn==3):
        return 'march'
    elif(dn==4):
        return 'april'
    elif(dn==5):
        return 'may'
    elif(dn==6):
        return 'june'
    elif(dn==7):
        return 'july'
    elif(dn==8):
        return 'august'
    elif(dn==9):
        return 'september'
    elif(dn==10):
        return 'october'
    elif(dn==11):
        return 'November'
    elif(dn==12):
        return 'December'
    else:
        return 'Invalid'

for i in range(3):
    inpNum=int(input())
    print(printMonth(inpNum))


