from cryptography.fernet import Fernet

'''def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)


def add():
    platform = input("Platform: ")
    name = input("Account name: ")
    pwd = input("Password: ")

    with open("password.txt", "a") as f:
        f.write(platform + " | " + name + " | " + fer.encrypt(pwd.encode()).decode() + "\n")

def view():
    with open("password.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            platf, user, pw = data.split("|")
            print("Platform:", platf, "| Username:", user, "| Password:", fer.decrypt(pw.encode()).decode())


while True:
    mode = input("Would you like to add a new password or view a password (add or view)? ")
    if mode == "q":
        break
    elif mode == "add":
        add()
    elif mode == "view":
        view()