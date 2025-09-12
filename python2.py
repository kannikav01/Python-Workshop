marks = int(input("enter marks"))
if marks >= 0 and marks <=100:
    if marks >= 80 and  marks <=100:
        print("A")
    elif marks >= 50 and marks <=79:
        print("B")
    elif marks >= 35 and marks <=49:
        print("C")
    else:
        print("fail")
else:
    print("invalid")