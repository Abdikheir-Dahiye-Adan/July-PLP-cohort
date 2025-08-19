file = open('input.pdf', 'w')
file.write("This is a test file.\n")
#  read a file
file = open('input.pdf', 'r')
data = file.read()
print(data)

# modifying the file
# appending a file
file = open('input.pdf', 'a')
file.write("The file contains important reading materials!")
# reading the file again
file = open('input.pdf', 'r')
data = file.read()
print(data)
# counting the words in the file
word_count = len(data.split())
print(word_count)

# changing the file to uppercase
uppercase_data = data.upper()
print(uppercase_data)
#  writing the modified version to anew file
output_file = open('output.pdf', 'w')
output_file.write(uppercase_data)
output_file.write(f"\nWord count:{word_count}")
print("modified content written to output.txt")
print("Success")

output_file.close()


# Error handling using try-except
try:
    file = open('input.pdf', 'r')
    data = file.read()
    print(data)
except FileNotFoundError:
    print("File not found. Please check the file path.")

