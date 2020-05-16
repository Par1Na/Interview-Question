# Interview-Question

def segregate(list, size): 

    j = 0

    for i in range(size): 

        if (list[i] <= 0): 

            list[i], list[j] = list[j], list[i] 

            j += 1 

    return j  

def findMissingPositive(list, size): 


    for i in range(size): 

        if (abs(list[i]) - 1 < size and list[abs(arr[i]) - 1] > 0): 

            list[abs(arr[i]) - 1] = -list[abs(arr[i]) - 1
    for i in range(size): 
        if (list[i] > 0):
            return i + 1

    return size + 1

def findMissing(list, size): 

    shift = segregate(list , size)

    return findMissingPositive(list[shift:], size - shift)  

list = [ 0, 10, 2, -10, -20 ] 

list_size = len(list) 

missing = findMissing(list, list_size)  

print("The smallest positive missing number is ", missing) 

  
