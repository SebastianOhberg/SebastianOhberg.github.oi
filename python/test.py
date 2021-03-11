#Test to refill an tic tac toe board


def draw():  
    board = ''

    for i in range(1):
        print (' -------' *3)
        print (' |     |' *3 )
        print (' |  x  |' + ' |     |' *2 )
        print (' |     |' *3 )
    print (' -------' *3)
    for i in range(1):
        print (' |     |' *3 )
        print (' |     |' *3 )
        print (' |     |' *3 )
    print (' -------' *3)
    for i in range(1):
        print (' |     |' *3 )
        print (' |     |' *3 )
        print (' |     |' *3 )
    print (' -------' *3)

draw()
row = 1
i = [1,2,3]
if (row == 1):
    i = [1,2,3]
    i[0] = 0
    print(i)

