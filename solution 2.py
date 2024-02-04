# downloaded from terminal - "pip install tabulate"
from tabulate import tabulate

# function
# file operation
# exception handling
def Introduction():
    try:
        look = open("intro.txt","r")
        print(look.read())
    except IOError:
        print ("file not found")
    except :
        print ("Something went wrong. Try again.")

Introduction()

# Usage of object oriented programming - class
class DataTable:
    def __init__(self, columns):
        # Initialize the DataTable with given columns and an empty rows dictionary.
        self.columns = columns
        self.rows = {}

    def add_row(self, index, values):
        while True:
            try:
                # Validate input and add a new row to the table.
                if index in self.rows:
                    raise ValueError(f"Row with index {index} already exists")

                if len(values) != len(self.columns):
                    raise ValueError("Number of values must match the number of columns")

                row_dict = dict(zip(self.columns, values))
                self.rows[index] = row_dict
                break
            except ValueError as e:
                print(f"Error: {e}")
                # Prompt for valid input if an error occurs during input validation.
                index = int(input("Enter a different index: "))
                values = input("Enter values (comma-separated): ").split(",")

    def edit_row(self, index, values):
        while True:
            try:
                # Validate input and add a new row to the table.
                if index not in self.rows:
                    raise ValueError(f"Row with index {index} does not exist")

                if len(values) != len(self.columns):
                    raise ValueError("Number of values must match the number of columns")

                row_dict = dict(zip(self.columns, values))
                self.rows[index] = row_dict
                break
            except ValueError as e:
                print(f"Error: {e}")
                # Prompt for valid input if an error occurs during input validation.
                index = int(input("Enter a different index: "))
                values = input("Enter new values (comma-separated): ").split(",")

    def delete_row(self, index):
        while True:
            try:
                # Validate input and add a new row to the table.
                if index not in self.rows:
                    raise ValueError(f"Row with index {index} does not exist")

                del self.rows[index]
                break
            except ValueError as e:
                print(f"Error: {e}")
                # Prompt for valid input if an error occurs during input validation.
                index = int(input("Enter a different index: "))

    def display_table(self):
        # Display the table in a formatted way using the tabulate library.
        table_data = []
        for index, row in self.rows.items():
            row_values = [index] + [row[col] for col in self.columns]
            table_data.append(row_values)

        headers = ["Index"] + self.columns
        table = tabulate(table_data, headers, tablefmt="fancy_grid", numalign="center")
        print(table)

# Example usage
columns = ["Time","Task"]
table = DataTable(columns)

while True:
    # Display options and prompt for user's choice
    table.display_table()
    print("\n1. Add Row\n2. Edit Row\n3. Delete Row\n4. Exit")
    choice = input("Enter your choice: ")

    # exception handling
    try:
        if choice == "1":
            # Prompt for input and add a new row to the table.
            index = int(input("Enter the index: "))
            values = input("Enter values (comma-separated): ").split(",")
            table.add_row(index, values)
        elif choice == "2":
            # Edit an existing row in the table.
            if not table.rows:
                print("Cannot edit. The table is empty.")
            else:
                index = int(input("Enter the index of the row to edit: "))
                values = input("Enter new values (comma-separated): ").split(",")
                table.edit_row(index, values)

        elif choice == "3":
            # Delete an existing row from the table
            if not table.rows:
                print("Cannot delete. The table is empty.")
            else:
                index = int(input("Enter the index of the row to delete: "))
                table.delete_row(index)

        elif choice == "4":
            # Exit the program.
            break
  
    except ValueError:
        # Invalid choice, prompt for user input again.
        print("Invalid choice. Please try again.")
