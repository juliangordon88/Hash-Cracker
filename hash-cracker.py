import hashlib


#pedimos el hash
hash_file = input("Enter the hash: ")

#pedimos la ruta al diccionario
dic_file = input("Enter the dictionary file path: ")

#leemos el diccionario
with open(dic_file, 'r') as file:

    diccionario = [line.strip() for line in file]

    for password in diccionario:
        #aqui debemos elegir el tipo de hash que queremos
        calculated_hash = hashlib.md5(password.encode()).hexdigest()

        #si lo encontramos en el diccionario
        if calculated_hash == hash_file:
            print("The password is: ", password)
            break
        #si no lo encontramos
        else:
            print("The password is not in the dictionary ")