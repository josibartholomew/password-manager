master_pwd = input("What is the master password? ")

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readLines():
            print(line)


def add():
    name = input("Account Name: ")
    pwd = input("PAssword: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + pwd + "\n")


while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), q to quit? ").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")