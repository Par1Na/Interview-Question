# Interview-Question


     size = int(input("Enter the number of
              string you want to add in the array: "))

     List = []

for i in range(size):

    List.append(input("Enter the string number " +
                       str(i + 1) + ": ").strip())

      prefix = List[0]

for i in range(1,size):

    while True:

        if List[i].startswith(prefix):

            break

        prefix = prefix[:-1]

      print("The largest prefix of the 
                 given string is \"" + prefix +"\"")
