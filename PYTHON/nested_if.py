X = 9
r = X % 2

if r == 0:
    print("even")
    if X > 5:
        print("greater")
    elif X < 5 :
        print("less")
else:
    print("odd")