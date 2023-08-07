while 1:
    test = list(map(int, input().split()))
    if test[0] == 0 and test[1] == 0:
        break

    if test[0] * test[1] == 0:
        print("neither")
    else:
        if test[0] > test[1]:
            if test[0] % test[1] == 0:
                print("multiple")
            else:
                print("neither")
        else:
            if test[1] % test[0] == 0:
                print("factor")
            else:
                print("neither")