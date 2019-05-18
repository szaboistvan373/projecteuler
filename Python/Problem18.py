class Coor:
    def __init__(self, x=None, y=None):
        self.x = x if x is not None else 0
        self.y = y if y is not None else 0


def build_triangle_array(array):
    builderArray = []

    currentLength = 0
    subarray = []
    requiredInsertLength = 1

    for x in input:
        subarray.append(x)
        currentLength += 1
        if currentLength == requiredInsertLength:
            builderArray.append(subarray)
            subarray = []
            currentLength = 0
            requiredInsertLength += 1

    triangleArray = []
    i = 0

    triangleHeight = len(builderArray)

    while i < len(builderArray):
        index = i
        subarray = []
        while index < triangleHeight:
            subarray.append(builderArray[index][-i - 1])
            index += 1
        triangleArray.append(subarray)
        i += 1

    return triangleArray


inputString = "75 95 64 17 47 82 18 35 87 10 20 04 82 47 65 19 01 23 75 03 34 88 02 77 73 07 63 67 99 65 04 28 06 16 70 92 41 41 26 56 83 40 80 70 33 41 48 72 33 47 32 37 16 94 29 53 71 44 65 25 43 91 52 97 51 14 70 11 33 28 77 73 17 78 39 68 17 57 91 71 52 38 17 14 91 43 58 50 27 29 48 63 66 04 68 89 53 67 30 73 16 69 87 40 31 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"

splitter = inputString.split(" ")

input = [int(x) for x in splitter]

triangle = build_triangle_array(input)

startingYIndex = len(triangle) - 2

currentCoor = Coor(0, startingYIndex)

while currentCoor.x > -1 and currentCoor.y > -1:
    startingCoor = Coor(currentCoor.x, currentCoor.y)
    while startingCoor.y > -1:
        triangle[startingCoor.y][startingCoor.x] += max(triangle[startingCoor.y + 1][startingCoor.x],
                                                        triangle[startingCoor.y][startingCoor.x + 1])
        startingCoor.x += 1
        startingCoor.y -= 1
    currentCoor.y -= 1

print(triangle[0][0])
