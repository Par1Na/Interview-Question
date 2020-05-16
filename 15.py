# Interview-Question


def arrayLeftRight(array):

    size = len(array)

    if array[0] <= min(array[1:]):

        return array[0]

    for i in range(1,size - 1):

        if max(array[:i]) <= array[i] <= min(array[i+1:]):

            return array[i]

    if max(array[:-1]) <= array[-1]:

        return array[-1]

size = int(input("Enter the size of array: "))

array = []

for i in range(size):

    array.append(int(input("Enter the element
          number " + str(i + 1) + " in the array: ")))

print("The first element such that all 
           if its left elements are smaller and
           all right elements are greater than it is"
                              , arrayLeftRight(array))
