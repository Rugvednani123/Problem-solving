import os

# 1. Create a new file and write data
try:
    file = open("student.txt", "w")

    file.write("Name: Rugved\n")
    file.write("Batch: 2026\n")
    file.write("Course: Python\n")

    file.close()

    print("File created successfully.")

except Exception as e:
    print("Error:", e)


# 2. Read the contents of the file
try:
    file = open("student.txt", "r")

    content = file.read()

    print("\nFile Content:")
    print(content)

    file.close()

except FileNotFoundError:
    print("File does not exist.")

except Exception as e:
    print("Error:", e)


# 3. Append data to the file
try:
    file = open("student.txt", "a")

    file.write("College: GNI\n")

    file.close()

    print("Data appended successfully.")

except FileNotFoundError:
    print("File does not exist.")

except Exception as e:
    print("Error:", e)


# 4. Read file after appending
try:
    file = open("student.txt", "r")

    print("\nFile Content After Appending:")
    print(file.read())

    file.close()

except FileNotFoundError:
    print("File does not exist.")

except Exception as e:
    print("Error:", e)


# 5. Check whether file exists
if os.path.exists("student.txt"):
    print("\nstudent.txt exists.")
else:
    print("\nstudent.txt does not exist.")


# 6. Copy contents to another file
try:
    file1 = open("student.txt", "r")
    content = file1.read()
    file1.close()

    file2 = open("student_copy.txt", "w")
    file2.write(content)
    file2.close()

    print("File copied successfully.")

except FileNotFoundError:
    print("Source file does not exist.")

except Exception as e:
    print("Error:", e)


# 7. Count number of lines
try:
    file = open("student.txt", "r")

    count = 0

    for line in file:
        count = count + 1

    file.close()

    print("Number of lines:", count)

except FileNotFoundError:
    print("File does not exist.")

except Exception as e:
    print("Error:", e)


# 8. Try to read a non-existing file
try:
    file = open("abc.txt", "r")

    print(file.read())

    file.close()

except FileNotFoundError:
    print("\nError: abc.txt does not exist.")

except Exception as e:
    print("Error:", e)