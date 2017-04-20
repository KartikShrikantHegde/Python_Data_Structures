# Seek is a pointer to keep track where we are in the file.

# Before reading or writing seek pointer is set to zero.

# it moves by one position after writing a character to file

# Before reading we must again set it back to zero.


# Eg: myFile = open("a.txt", "r")
#
#     myFile.read(10)           read 10 bytes
#     myFile.seek(0)            set back to zero to read from begining again


# closing the file and reopening the file will set the seek pointer to zero position again