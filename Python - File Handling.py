import os


# 1. Create a new file and write content
def create_file(filename, text):
    try:
        file = open(filename, "w")
        file.write(text)
        file.close()
        print("File created and data written successfully.")

    except Exception as e:
        print("Error:", e)


# 2. Read an existing file
def read_file(filename):
    try:
        file = open(filename, "r")
        content = file.read()
        file.close()

        print("File Content:")
        print(content)

    except FileNotFoundError:
        print("Error: File does not exist.")

    except Exception as e:
        print("Error:", e)


# 3. Append data to an existing file
def append_file(filename, text):
    try:
        file = open(filename, "a")
        file.write(text)
        file.close()
        print("Data appended successfully.")

    except FileNotFoundError:
        print("Error: File does not exist.")

    except Exception as e:
        print("Error:", e)


# 4. Copy contents from one file to another
def copy_file(source, destination):
    try:
        file1 = open(source, "r")
        content = file1.read()
        file1.close()

        file2 = open(destination, "w")
        file2.write(content)
        file2.close()

        print("File copied successfully.")

    except FileNotFoundError:
        print("Error: Source file does not exist.")

    except Exception as e:
        print("Error:", e)


# 5. Check whether a file exists
def check_file(filename):
    if os.path.exists(filename):
        print("File exists.")
    else:
        print("File does not exist.")


# 6. Count number of lines in a file
def count_lines(filename):
    try:
        file = open(filename, "r")

        count = 0

        for line in file:
            count = count + 1

        file.close()

        return count

    except FileNotFoundError:
        print("Error: File does not exist.")
        return 0

    except Exception as e:
        print("Error:", e)
        return 0


# Main program
def main():

    print("----- CREATE FILE -----")
    create_file(
        "student.txt",
        "Name: Rugved\n"
        "Batch: 2026\n"
        "Course: Python\n"
    )

    print("\n----- READ FILE -----")
    read_file("student.txt")

    print("\n----- APPEND FILE -----")
    append_file(
        "student.txt",
        "College: GNI\n"
    )

    print("\n----- READ FILE AFTER APPENDING -----")
    read_file("student.txt")

    print("\n----- CHECK FILE -----")
    check_file("student.txt")

    print("\n----- COPY FILE -----")
    copy_file("student.txt", "student_copy.txt")

    print("\n----- READ COPIED FILE -----")
    read_file("student_copy.txt")

    print("\n----- COUNT LINES -----")
    lines = count_lines("student.txt")
    print("Number of lines:", lines)

    print("\n----- CHECK NON-EXISTING FILE -----")
    check_file("abc.txt")

    print("\n----- READ NON-EXISTING FILE -----")
    read_file("abc.txt")


main()