usrnme = input("Enter username: ")
msg = input("Write message: ")

while msg:
    file = open("logs/history.txt", "w")
    text = ["asd\n"]
    file.writelines(text)
    file = open("logs/history.txt")
    content = file.read()
    file.close()
    print(content)
    msg = input("Write message: ")