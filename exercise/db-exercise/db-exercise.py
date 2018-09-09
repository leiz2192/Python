#!/usr/bin/python
# -*- coding:utf-8 -*-

import json
import pymysql
import sqlite3

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base

mysql_engine = create_engine("mysql+pymysql://leiz:leiz@198.168.1.107:3306/test")
sqlite_engine = create_engine("sqlite:///{0}".format("test.db"))

MySQLSession = sessionmaker(bind=mysql_engine)
SQLiteSession = sessionmaker(bind=sqlite_engine)

Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(String(20), primary_key=True)
    name = Column(String(20))


def orm_sqlalchemy():
    mysql_session = MySQLSession()
    user = mysql_session.query(User).filter(User.id == '1').one()
    print("orm_sqlalchemy mysql: ", user.id, user.name)
    mysql_session.close()

    sqlite_session = SQLiteSession()
    sqlite_session.add(User(id='2', name='Bob'))
    sqlite_session.commit()
    user = sqlite_session.query(User).filter(User.id == '2').one()
    print("orm_sqlalchemy sqlite: ", user.id, user.name)
    sqlite_session.close()


def db_sqlalchemy():
    db_session = Session(bind=mysql_engine)
    db_data = db_session.execute("select * from user").fetchall()
    print("db_sqlalchemy, mysql: {0}".format(db_data))
    db_session.close()

    db_session = Session(bind=sqlite_engine)
    db_data = db_session.execute("select * from user").fetchall()
    print("db_sqlalchemy, sqlite: {0}".format(db_data))
    db_session.close()


def db_sqlite():
    db_conn = sqlite3.connect("test.db")
    db_cursor = db_conn.cursor()
    # db_cursor.execute("create table user (id varchar(20) primary key, name varchar(20))")
    # db_cursor.execute("insert into user(id, name) values('{0}', '{1}')".format("1", "Michael"))
    db_cursor.execute("select * from user")
    db_data = db_cursor.fetchall()
    db_conn.commit()
    db_cursor.close()
    db_conn.close()

    print("db_sqlite: {0}".format(db_data))


def db_mysql():
    db_conn = pymysql.connect("198.168.1.107", "leiz", "leiz", "test")
    db_cursor = db_conn.cursor()
    # db_cursor.execute("insert into user(id, name) values('{0}', '{1}')".format("2", "Putty"))\
    db_cursor.execute("select * from user")
    db_data = db_cursor.fetchall()
    db_conn.commit()
    db_cursor.close()
    db_conn.close()

    print("db_mysql: {0}".format(json.dumps(db_data)))


def main():
    db_mysql()
    db_sqlite()
    db_sqlalchemy()
    orm_sqlalchemy()


if __name__ == '__main__':
    main()
