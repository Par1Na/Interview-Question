# Interview-Question


def segregate(arr): 

    res = ([x for x in arr if x==0] + [x for x in arr if x==1]) 

    print(res) 

if __name__ == "__main__": 

    arr = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]  

    segregate(arr) 
