def convertInt(arr):
    output = []
    for number in arr:
        output.append(int(number))
    return output


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
        try:
            matrix.append(convertInt(elements))
        except:
            ifValid = False
            break

    if ifValid:
        return matrix
    else:
        return False


file1 = open("a.txt", "r")
a = readMatrix(file1)
file1.close()
if a:
    rowA = len(a)
    colomnA = len(a[0])
    file2 = open("b.txt", "r")
    b = readMatrix(file2)
    file2.close()
    if b:
        rowB = len(b)
        colomnB = len(b[0])
        if colomnA == colomnB:
            multi = []
            for i in range(rowA):
                row = []
                for j in range(colomnA):
                    row.append(a[i][j] * b[i][j])
                multi.append(row)
            for r in multi:
                print(*r)
        else:
            print("cannot multiply!!")
    else:
        print("Invalid Matrix B!!")
else:
    print("Invalid Matrix A!!")
