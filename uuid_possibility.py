def get_quantity(p, n):
    total = (2 ** 8) ** n
    q = 1.0
    x = 0
    while 1 - q < p:
        q *= (total - x)/total
        x += 1
    return x - 1


def get_possibility(x, n):
    total = (2 ** 8) ** n
    p = 1.0
    for i in range(total, total - x, -1):
        p *= i/total
    return 1 - p


if __name__ == '__main__':
    text = 'y'
    while True:
        text = input("Do you want to calculate quantity or possibility? \nQuantity(q)\nPossibility(p)\nQuit(n)\n")
        if text == 'q':
            p = input("What the possibility do you want to have?\n")
            n = input("What is the digits of your uuid?\n")
            p = float(p)
            n = int(n)
            x = get_quantity(p, n)
            print(f"You can generate {x} uuids under the possibility {p} of collision\n")
        elif text == 'p':
            x = input("What is the quantity of uuids you want to generate?\n")
            n = input("What is the digits of your uuid?\n")
            x = int(x)
            n = int(n)
            p = get_possibility(x, n)
            print(f"If you generate {x} uuids, there is a possibility {p} of collision\n")
        elif text == 'n':
            break
        else:
            print("Wrong input")
