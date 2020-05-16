# Interview-Question


size = int(input("Enter the number of 
                       elements in the List: "))
    List = []

for i in range(size):

    List.append(int(input("Enter the element " + 
                      str(i + 1) + " in the List: ")))

    a, b, c = sorted(List)[-3:]

     print("The highest product possible by 
              multiplying 3 numbers from the list is ",
                    ,a * b * c)
