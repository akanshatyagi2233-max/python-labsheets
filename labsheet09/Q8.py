products = {}

while True:
    print("\n1. Add Product")
    print("2. View Products")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        pid = input("Enter product ID: ")
        name = input("Enter product name: ")
        price = float(input("Enter price: "))
        products[pid] = {"name": name, "price": price}
        print("Product added!")

    elif choice == 2:
        print(products)

    elif choice == 3:
        pid = input("Enter product ID: ")
        if pid in products:
            products[pid]["price"] = float(input("Enter new price: "))
            print("Product updated!")
        else:
            print("Product not found")

    elif choice == 4:
        pid = input("Enter product ID: ")
        if pid in products:
            del products[pid]
            print("Product deleted!")
        else:
            print("Product not found")

    elif choice == 5:
        break

    else:
        print("Invalid choice")
