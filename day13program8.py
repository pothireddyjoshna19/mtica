spins=[('red', '18'),('black', '13'),('red', '5'),
       ('red', '5'),('red', '9'),('black', '38'),
       ('red', '15'),('black', '20'),('red', '14'),
       ('red', '16'),('black', '34'),('red', '21')]


def countReds(aList):
    count=0
    for color,number in aList:
        if color == 'black':
            yield count
            count=0
        else:
            count +=1
    yield count

gaps= [ gap for gap in countReds(spins) ]
print (gaps)
