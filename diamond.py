rowSize = int(input("enter the number of rows: "))
if rowSize % 2 == 0: 
    halfDiamond = int(rowSize/2)
else:
    halfDiamond = int(rowSize/2) + 1
space = halfDiamond-1

print(halfDiamond, space)