def readMatrix(file):
    ifValid = True
    lines = file.read().split("\n")
    rows = len(lines)
    matrix = []
    prelen = None
    for line in lines:
        elements = line.split()
        if prelen is None:
            prelen = len(elements)
        elif prelen != len(elements):
            ifValid = False
            break
        matrix.append(elements)
    if ifValid:
        return matrix
    else:
        return False


file1 = open("a.txt", "r")
a = readMatrix(file1)
file1.close()
print(a)
if a:
    file2 = open("b.txt", "r")
    b = readMatrix(file2)
    file2.close()
    print(b)
else:
    print("Invalid Matrix A!!")
