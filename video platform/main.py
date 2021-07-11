import pymysql
import datetime
import hashlib
import backend
from termcolor import colored


class Main:
    def __init__(self):
        self.connection = pymysql.connect(host="localhost", user="root", password="12341234",port=3306, database="youtube")
        self.cursor = self.connection.cursor()
        self.userId = 0

    def signup(self):
        username = ''
        pas = ''
        email = ''
        z = True
        while (username == '') | z:
            username = input("Enter Username: ")
            self.cursor.execute("SELECT `username` FROM `user` where `username`=%s", (username,))
            result = self.cursor.fetchone()
            if result:
                print('Username Is Already Taken!')
            else:
                break

        while pas == '':
            pas = input("Enter Password: ")

        while email == '':
            email = input("Enter Email: ")
        hashed_password = hashlib.sha512((pas).encode('utf-8')).hexdigest()
        self.cursor.execute("INSERT INTO `user` (`username`, `pass`, `email`, `date`) VALUES (%s, %s, %s, %s)",
                            (username, hashed_password[:15], email, datetime.datetime.now()))
        self.connection.commit()
        sql = "SELECT * FROM `user` WHERE `username`=%s"
        self.cursor.execute(sql, (username,))
        result = self.cursor.fetchone()
        self.userId = result[1]
        self.cursor.execute("INSERT INTO `playlist` (`playlistName`, `userId`) VALUES (%s, %s)",
                            ('watch later', self.userId))
        self.connection.commit()
        print('\nsigned up--------------------\n')
        print(
            '1: Create New PlayList\n'
            '2: my playlists\n'
            '3: View Videos\n'
            '4: View Channels\n'
            '5: Create New Channel\n'
            '6: Upload New Video\n'
            '7: Search\n'
            '8: Exit\n'
            '----------------------------------------')
        m = backend.Video(self.userId)
        m.main()

    def main(self):
        x = input('1)Login\n2)Sign Up\n\nchoice:\n')
        if x == '1':
            self.login()
        elif x == '2':
            self.signup()

    def login(self):
        while True:
            name = input('Username: ')
            password = input('Password: ')
            hashed_password = hashlib.sha512((password).encode('utf-8')).hexdigest()
            self.cursor.execute("SELECT * FROM `user` WHERE `username`=%s and `pass`=%s", (name, hashed_password[:15]))
            result = self.cursor.fetchone()
            if result:
                print('\nlogged in--------------------\n')
                print(
                    '1: Create New PlayList\n'
                    '2: my playlists\n'
                    '3: View Videos\n'
                    '4: View Channels\n'
                    '5: Create New Channel\n'
                    '6: Upload New Video\n'
                    '7: Search\n'
                    '8: Exit\n'
                    '----------------------------------------')
                self.userId = result[1]
                m = backend.Video(self.userId)
                m.main()
                break
            else:
                print('Wrong Username Or Password. please try again')


x = Main()
x.main()
