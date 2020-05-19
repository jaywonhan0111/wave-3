def shipping_calculator(num_items):
    if num_items > 0:
        return 10.95 +(num_items - 1) * 2.95

    else:
        return 0

def main():
    num_items = int(input("Enter the number of items for shipping"))
    fee = shipping_calculator(num_items)
    print("Shipping charge: " + str(fee))

if __name__ == "__main__":
    main()

    