class Coor:
    def __init__(self):
        self.x = 0
        self.y = 0


class BackTrackSolver:
    def __init__(self, triangleArray, maxValue):
        self.triangleArray = triangleArray
        self.maxValueInTrianlge = maxValue
        self.n = len(triangleArray) - 1

    def solve(self):
        jelenlegi = []
        optimalis = []
        for i in range(self.n):
            jelenlegi.append(True)
            optimalis.append(True)
        self.back_track(0, jelenlegi, optimalis)
        return self.sum_value(optimalis)


    def sum_value(self, path):
        stepCount = 0
        coordinates = Coor()
        sum = 0

        while stepCount < self.n:
            if path[stepCount]:
                coordinates.x += 1
            else:
                coordinates.y += 1
            sum += triangleArray[coordinates.x][coordinates.y]
            stepCount += 1
        return sum

    def best_solution_from_here(self, level, jelenlegi):
        best = (self.n - level) * self.maxValueInTrianlge
        return best

    def clone_array(self, array):
        returnArray = []
        for i in array:
            returnArray.append(i)
        return returnArray



    def back_track(self, level, jelenlegi, optimalis):
        for i in range(2):
            jelenlegi[level] = i == 0
            if level == self.n - 1:
                if self.sum_value(jelenlegi) > self.sum_value(optimalis):
                    optimalis = self.clone_array(jelenlegi)
            else:
                if self.sum_value(jelenlegi) + self.best_solution_from_here(level, jelenlegi) > self.sum_value(optimalis):
                    self.back_track(level + 1, jelenlegi, optimalis)


array = []
inputString = "75 95 64 17 47 82 18 35 87 10 20 04 82 47 65 19 01 23 75 03 34 88 02 77 73 07 63 67 99 65 04 28 06 16 70 92 41 41 26 56 83 40 80 70 33 41 48 72 33 47 32 37 16 94 29 53 71 44 65 25 43 91 52 97 51 14 70 11 33 28 77 73 17 78 39 68 17 57 91 71 52 38 17 14 91 43 58 50 27 29 48 63 66 04 68 89 53 67 30 73 16 69 87 40 31 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"
splitter = inputString.split(" ")

input = [int(x) for x in splitter]

builderArray = []

currentLength = 0
subarray = []
requiredInsertLength = 1
maxValueInTrianlge = max(input)

for i in range(len(input)):
    subarray.append(input[i])
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


def whichWayIsBetter(triangleArray, coor):
    return triangleArray[coor.x][coor.y + 1] < triangleArray[coor.x + 1][coor.y]


stepCount = 0
coordinates = Coor()
sum = triangleArray[0][0]

while stepCount < triangleHeight - 1:
    if whichWayIsBetter(triangleArray, coordinates):
        coordinates.x += 1
    else:
        coordinates.y += 1
    sum += triangleArray[coordinates.x][coordinates.y]
    stepCount += 1

solver = BackTrackSolver(triangleArray, maxValueInTrianlge)

print(solver.solve())