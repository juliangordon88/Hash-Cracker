import hashlib

hash_file = input("Enter the hash: ")

dic_file = input("Enter the dictionary file path: ")

with open(dic_file, 'r') as file:

    diccionario = [line.strip() for line in file]

    for password in diccionario:

        calculated_hash = hashlib.md5(password.encode()).hexdigest()

        if calculated_hash == hash_file:
            print("The password is: ", password)
            break
        else:
            print("The password is not in the dictionary ")