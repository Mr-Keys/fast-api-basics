from sqlalchemy.orm.session import Session
from schemas import UserBase
from db.models import DbUser
from db.hash import encrypt, decrypt


def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        username=request.username,
        email=request.email,
        password=encrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_all_users(db: Session):
    return db.query(DbUser).all()


def get_user(db: Session, id):
    return db.query(DbUser).filter(DbUser.id == id).first()


def update_user(db: Session, id, request: UserBase):
    user = db.query(DbUser).filter(DbUser.id == id)
    user.update({
        DbUser.username: request.username,
        DbUser.email: request.email,
        DbUser.password: encrypt(request.password)
    })
    db.commit()
    return 'ok'


def delete_user(db: Session, id):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    #handle any exceptions
    db.delete(user)
    db.commit()
    return 'ok'
