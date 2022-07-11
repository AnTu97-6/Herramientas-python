import hashlib


def main():
    clave = input("Ingresa el hash:  ")

    md5 = hashlib.md5(clave.encode("utf")).hexdigest()
    print("Esto es un hash md5: " + md5)
    print("longuitud: {}".format(len(md5)))

    sha1 = hashlib.sha1(clave.encode("utf")).hexdigest()
    print("Esto es un hash sha1: " + sha1)
    print("longuitud:{}".format(len(sha1)))

    sha224 = hashlib.sha224(clave.encode("utf")).hexdigest()
    print("Esto es un hash sha224: " + sha224)
    print("longuitud:{}".format(len(sha224)))

    sha256 = hashlib.sha256(clave.encode("utf")).hexdigest()
    print("Esto es un hash sha256: " + sha256)
    print("longuitud: {}".format(len(sha256)))

    sha384 = hashlib.sha384(clave.encode("utf")).hexdigest()
    print("Esto es un hash sha384: " + sha384)
    print("longuitud:{}".format(len(sha384)))


main()
