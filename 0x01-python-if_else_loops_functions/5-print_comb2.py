for num in range(100):
    if num == 99:
        print("{}".formatt(num))
    else:
        print("{:02}".format(num), end=", ")
