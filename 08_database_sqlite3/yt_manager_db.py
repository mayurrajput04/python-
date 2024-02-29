import sqlite3

conn = sqlite3.connect('yt_manager.db')

cursor = conn.cursor()

cursor.execute(''' 
    CREATE VIDEOS OF NOT EXIST VIDEOS(
        id INTEGER PRIMARY KEY
        name TEXT NOT NULL
        time TEXT NOT NULL
    )
''')


def list_all_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name ,time):
    cursor.execute("INSERT INTO videos(name,time) , VALUE (?,?)",(name ,time))
    cunn.commit()

def update_video(video_id ,name ,time):
    cursor.execute("UPDATE videos SET name = ? time = ? WHERE  id = ?", (name , time ,video_id))
    cunn.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos where video_id =?",(video_id , ))
     #it takes input in the format of tuple only 
    cunn.commit()
    pass


def main():
    videos =[]
    print("\n Youtube Manager with Database | choose your option ")
    print("1.List Videos")
    print("2.Add Videos")
    print("3.Update VIdoes")
    print("4.Delete Video")
    print("5.Exit Program")

    choice = input("Enter your choice :")

    match choice :
        case '1':
            list_all_videos(videos)
        case '2':
            name = print("Enter video name: ")
            time = print("Enter video time: ")
            add_video(name,time)
        case '3':
            video_id = print("Enter video ID to update: ")
            name = print("Enter video name: ")
            time = print("Enter video time: ")
            update_video(video_id ,name ,time)
        case '4':
            video_id = print("Enter video ID to update: ")
            delete_video(video_id)    
        case '5':
            break
        case _ :
            print("Enter valid choice.")
    conn.close()



if __name__ = "__main__":
    main()
