import pymysql

from app.secrets import get_secret


def connect(host_name: str, username: str, port: str, passwor: str, db_name: str):
    return pymysql.connect(host_name, user=username, port=port,
                           passwd=passwor, db=db_name)


def create_db(host_name:str, username:str, port:str, secret_name:str, db_name:str):
    password = get_secret("db_conn_secret")
    db_conn = connect(host_name, username, port, password, db_name)
    return db_conn

