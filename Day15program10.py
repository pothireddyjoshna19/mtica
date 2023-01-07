def F():

    x=10
    print('id(x) in f outer:',id(x))
    def g():
        nonlocal x
        x = 15
        print('id(x) in f inner:',id(x))
    g()
    print(x)

F()
