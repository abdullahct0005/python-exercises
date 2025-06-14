
# Exercise 1: Read and display file contents
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print("File Contents:\n", content)
    except Exception as e:
        print("Error reading file:", e)

# Exercise 2: Copy contents of one file to another
def copy_file(source, destination):
    try:
        with open(source, 'r') as src, open(destination, 'w') as dest:
            dest.write(src.read())
            print("File copied successfully.")
    except Exception as e:
        print("Error copying file:", e)

# Exercise 3: Count number of words in a file
def count_words(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            words = text.split()
            print("Total number of words:", len(words))
    except Exception as e:
        print("Error counting words:", e)

# Exercise 4: Convert string to integer using exception handling
def convert_to_int():
    try:
        user_input = input("Enter a number: ")
        number = int(user_input)
        print("Integer:", number)
    except ValueError:
        print("Invalid input! Not a valid integer.")

# Exercise 5: Raise exception if any number is negative
def check_for_negatives():
    try:
        nums = list(map(int, input("Enter a list of integers (space separated): ").split()))
        for num in nums:
            if num < 0:
                raise ValueError("Negative number found!")
        print("All numbers are non-negative.")
    except ValueError as e:
        print("Error:", e)

# Exercise 6: Average with exception handling and finally block
def compute_average():
    try:
        nums = list(map(int, input("Enter integers to calculate average (space separated): ").split()))
        avg = sum(nums) / len(nums)
        print("Average:", avg)
    except Exception as e:
        print("An error occurred:", e)
    finally:
        print("Program has finished running.")

# Exercise 7: Write to file with welcome message
def write_to_file():
    try:
        filename = input("Enter filename to write to: ")
        data = input("Enter text to write: ")
        with open(filename, 'w') as file:
            file.write(data)
        print("Welcome! File written successfully.")
    except Exception as e:
        print("An error occurred:", e)
