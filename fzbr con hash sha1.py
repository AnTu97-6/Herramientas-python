import hashlib


def main():
    resolverhash = input("hash a resolver: ")
    resolvedor = open("diccionario.txt", "r")

    for x in resolvedor.readlines():
        a = x.strip("\n")
        a = hashlib.sha1(a.encode("utf")).hexdigest()
        if a == resolverhash:
            print("Contrasena: {} con el hash sha1: {}".format(x, a))


main()
