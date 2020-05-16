# Interview-Question


s = input("Enter the number: ")

     sL = str(s)

      l = len(s) - 2

     Min = s[-1]

for i in range(l, -1, -1):

    a = s[i]
    if a < Min:
        s = s[:i] + Min + a + s[l:i:-1]
        break

if sL == s:

    print("Sorry! No number greater than the given number can be formed using the same digits of the given number.")

else:

    print("The next greater number from the given number which is formed by the same digits of the given number is",s)
