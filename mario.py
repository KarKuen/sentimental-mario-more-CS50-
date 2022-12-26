while True:
    height = input("Height: ")
    try:
        height = int(height)
        if 8 >= height > 0:
            break
    except:
        pass

for x in range(height):
    print(" " * (height - x - 1), end="")
    print("#" * (x + 1), end="")
    print(" " * 2, end="")
    print("#" * (x + 1), end="")
    print("")