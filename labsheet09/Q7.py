books = []

while True:
    print("\n1. Add Book")
    print("2. View Books")
    print("3. Update Book")
    print("4. Delete Book")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        book = input("Enter book name: ")
        books.append(book)
        print("Book added!")

    elif choice == 2:
        print("Books:", books)

    elif choice == 3:
        old = input("Enter old book name: ")
        if old in books:
            new = input("Enter new book name: ")
            books[books.index(old)] = new
            print("Book updated!")
        else:
            print("Book not found")

    elif choice == 4:
        book = input("Enter book name: ")
        if book in books:
            books.remove(book)
            print("Book deleted!")
        else:
            print("Book not found")

    elif choice == 5:
        break

    else:
        print("Invalid choice")
