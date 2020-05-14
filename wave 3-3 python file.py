def hypotenuse(s1, s2):
    return (s1 * s1 + s2 * s2) ** 0.5


def main():
    s1 = float(input("Enter length of first side: "))
    s2 = float(input("Enter length of second side: "))
    print("Length of the hypotenuse is", hypotenuse(s1, s2))


main()