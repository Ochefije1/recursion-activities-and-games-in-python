

file = open('comments.txt', 'a')
content = file.write("This is the second line of this text\n")
file.close()

file = open('comments.txt', 'r')
print(file.read())