set1 = {10,20,30,40,50}
set2 = {15,20,45,30,55}

if set1.isdisjoint(set2):
    print("Two sets have no items in common")
else:
    print("Two sets have items in common")
    print(set1.intersection(set2))

