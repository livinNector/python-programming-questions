'''
Write a function data_type_ops() that takes an integer, a float, a string, a list, a dictionary, and a set as input.
The function should perform the following operations:
1. Add 5.0 to the integer.
2. Divide the float by 2
3. Concatenate the string with your name.
4. Append  a new value  to the list.
5. Add a new key-value pair to the dictionary with key "new_key" and value "new_value".
6. Add a value v to the set.

'''

def data_type_ops(integer, floating, string, lst, dct, st, new_value, v):

    updated_integer = integer + 5.0

    # 2. Divide the float by 2
    updated_float = floating / 2

    # 3. Concatenate the string with your name
    updated_string = string + " Kaushik"

    # 4. Append a new value to the list
    lst.append(new_value)

    # 5. Add a new key-value pair to the dictionary
    dct["new_key"] = "new_value"

    # 6. Add a value to the set
    st.add(v)

    return updated_integer, updated_float, updated_string, lst, dct, st

'''
Write a function num_processor() that takes a list of integers and performs the following operations:
1. Filter out all even numbers.
2. Square the remaining odd numbers.
3. Return the sum of the squared numbers.

'''
def num_processor(num_list):

    # 1. Filter out even numbers
    odd_numbers = filter(lambda x: x % 2 != 0, num_list)

    # 2. Square the remaining odd numbers
    squared_numbers = [x**2 for x in odd_numbers]

    # 3. Return the sum of the squared numbers
    return sum(squared_numbers)

'''
Write a program that reads a string and prints the number of vowels in it.
'''
def count_vowels(string):
    """Count the number of vowels in a string."""
    vowels = "aeiouAEIOU"
    count = sum(1 for char in string if char in vowels)
    return count

'''
4. LIBRARY MANAGEMENT SYSTEM
'''

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book):

        self.books[book] = self.books.get(book, 0) + 1
        print(f'Book "{book}" added to the library.')

    def borrow_book(self, book):

        if self.books.get(book, 0) > 0:
            self.books[book] -= 1
            print(f'You borrowed "{book}".')
        else:
            print(f'Sorry, "{book}" is not available.')

    def return_book(self, book):

        self.books[book] = self.books.get(book, 0) + 1
        print(f'Book "{book}" returned to the library.')

    def display_inventory(self):

        if not self.books:
            print("The library is empty.")
        else:
            print("Current inventory:")
            for book, count in self.books.items():
                print(f'{book}: {count} copies')

def main():
    library = Library()
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Display Inventory")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            book = input("Enter the name of the book to add: ")
            library.add_book(book)
        elif choice == "2":
            book = input("Enter the name of the book to borrow: ")
            library.borrow_book(book)
        elif choice == "3":
            book = input("Enter the name of the book to return: ")
            library.return_book(book)
        elif choice == "4":
            library.display_inventory()
        elif choice == "5":
            print("Exiting the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()