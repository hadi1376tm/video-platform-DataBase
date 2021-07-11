import pymysql


connection = pymysql.connect(host="localhost", user="root", password="12341234", port=3306, database="youtube")
cursor = connection.cursor()

user = """CREATE TABLE user (
                            username varchar(30)  NOT NULL,
                            userId int(15) NOT NULL AUTO_INCREMENT,
                            pass varchar(30)  NOT NULL,
                            email varchar(40)  NOT NULL,
                            date varchar(30) ,
                            profileImage varchar(30),
                            PRIMARY KEY (userId)
)"""

video = """CREATE TABLE video (
                            videoId int(15) NOT NULL AUTO_INCREMENT,
                            videoName varchar(30)  NOT NULL,
                            StorageId varchar (20) UNIQUE,
                            videoCaption text(100) NOT NULL,
                            time varchar(30)  NOT NULL,
                            date varchar(30)  NOT NULL,
                            thumbnail varchar(40),
                            views int(15) NOT NULL,
                            likes int(15) NOT NULL,
                            dislikes int(15) NOT NULL,
                            PRIMARY KEY (videoId)
                            
)"""

comment = """CREATE TABLE comment (
       commentId int(15) NOT NULL AUTO_INCREMENT,
       userId int(15) NOT NULL,
       videoId int(15) NOT NULL,
       comment text(100) NOT NULL,
       PRIMARY KEY (commentId),
       FOREIGN KEY (videoId)
        REFERENCES video(videoId) ON DELETE CASCADE
)"""

channel = """CREATE TABLE channel (
    channelId   int(15) NOT NULL AUTO_INCREMENT,
    userId      int(15) NOT NULL,
    channelName varchar(30) NOT NULL,
    date        varchar(30) NOT NULL,
    chCaption   text(100) NOT NULL,
    PRIMARY KEY (channelId)
)"""

Channelcontent = """CREATE TABLE Channelcontent(
     userId  int(15) NOT NULL,
     videoId int(15) NOT NULL,
     channelId int(15) NOT NULL,
     FOREIGN KEY (channelId) REFERENCES channel(channelId)
    ON DELETE CASCADE
)"""

view = """CREATE TABLE view(
     userId  int(15) NOT NULL,
     videoId int(15) NOT NULL
)"""

reply = """CREATE TABLE reply  (
       parentId int(15) NOT NULL,
       childCom int(15) NOT NULL,
       videoId int(15) NOT NULL

)"""

likes = """CREATE TABLE likes (
     userId int(15) NOT NULL,
     videoId int(15) NOT NULL,
     FOREIGN KEY (videoId)
        REFERENCES video(videoId) ON DELETE CASCADE
)"""

dislikes = """CREATE TABLE dislikes (
     userId int(15) NOT NULL,
     videoId int(15) NOT NULL,
     FOREIGN KEY (videoId)
        REFERENCES video(videoId) ON DELETE CASCADE
)"""

joinChannel = """CREATE TABLE joinChannel(
        userId int(15) NOT NULL,
        channelId int(15) NOT NULL
)"""

playlist = """CREATE TABLE playlist(
         playlistId int(15) NOT NULL AUTO_INCREMENT,
         playlistName varchar(30) NOT NULL,
         userId int(15) NOT NULL,
         PRIMARY KEY (playlistId)
)"""

playlist_video = """CREATE TABLE playlist_video(
         playlistId int(15) NOT NULL,
         videoId int(15) NOT NULL
)"""



cursor.execute(user)
cursor.execute(video)
cursor.execute(channel)
cursor.execute(Channelcontent)
cursor.execute(view)
cursor.execute(likes)
cursor.execute(dislikes)
cursor.execute(joinChannel)
cursor.execute(playlist)
cursor.execute(playlist_video)
cursor.execute(comment)
cursor.execute(reply)

connection.close()
