# Interview-Question



     size = int(input("Enter the number 
                       of elements in array: "))

       List = []

for i in range(size):

    List.append(float(input("Enter the element number"
                        + str(i + 1) + ": ")))

triplet = set()

for i in range(size - 2):

    for j in range(i + 1, size - 1):

        for k in range(j + 1, size):

            if 1 < List[i] + List[j] + List[k] < 2:

         triplet.add(str((List[i], List[j], List[k])))

if len(triplet) == 0:

    print("The given numbers does not contain any
               triplet of the given condition type.")

else:

    print("The given numbers contains the
              following triplet of the given 
               condition type: ", ", ".join(triplet))
