from passlib.hash import bcrypt


def encrypt(password: str):
    return bcrypt.hash(password)


def decrypt(hashed_password, plain_password):
    return bcrypt.verify(plain_password, hashed_password)
