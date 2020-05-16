# Interview-Question


size = int(input("Enter the size of List: "))

     List = []

for i in range(size):

    List.append(int(input("Enter the element " + 
                      str(i + 1) + " in the List: ")))

      k = int(input("Enter the value of K: "))

print(sorted(List)[k-1])
