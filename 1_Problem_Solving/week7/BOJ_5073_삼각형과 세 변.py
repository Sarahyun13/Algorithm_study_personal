while True:
    a, b, c = map(int,input().split())
    if(a == b == c == 0):
        break
    
    big1 = a
    big2, big3 = b, c
    if big1 < b:
        big1 = b
        big2, big3 = a, c
    if big1 < c:
        big1 = c
        big2, big3 = a, b
    
    if(big1 >= big2 + big3):
        print("Invalid")
    elif(a == b == c):
        print("Equilateral")
    elif(a==b or b==c or a==c):
        print("Isosceles")
    elif(a!=b and b!=c and a!=c):
        print("Scalene")