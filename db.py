import pymysql

from app.secrets import get_secret


def connect(host_name: str, username: str, port: str, passwor: str, db_name: str):
    return pymysql.connect(host_name, user=username, port=port,
                           passwd=passwor, db=db_name)


def create_db(host_name:str, username:str, port:str, secret_name:str, db_name:str):
    db_secret = get_secret("db_conn_secret")
    db_conn = connect(db_secret["host_name"], db_secret["username"], db_secret["port"], db_secret["password"], db_secret["db_name"])
    return db_conn

