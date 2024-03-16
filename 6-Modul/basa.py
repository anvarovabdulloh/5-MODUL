import sqlite3


class Database:
    def init(self):
        self.connection = sqlite3.connect("abdulloh.db")
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            create table if not exists user(
                id integer primary key ,
                username varchar not null ,
                password varchar not null ,
                email varchar ,
                country varchar ,
                age integer ,
                phone_number varchar not null )
        """)
        ("insert into user (username, password, email, country, age, phone_number) values (?, ?, ?, ?, ?, ?)",
         (username, password, email, country, age, phone_number))
        self.connection.commit()

    def login_user(self, username, password):
        user = self.cursor.execute("select * from user where username=? and password=?",
                                   (username, password)).fetchone()
        return user

