for row in range(5):
    for col in range(4):
        if col==0 or ((row==0 or row==2 or row==4) and (col>0)):
            print("*",end="")
        else:
            print(end=" ")
    print()