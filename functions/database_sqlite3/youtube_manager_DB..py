import sqlite3
con = sqlite3.connect('youtube_videos.db')
cursor = con.cursor()

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL      
    )
''')
def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)
def add_videos(name,time):
    cursor.execute("INSERT INTO videos (name,time)VALUES (?,?)" , (name,time))
    con.commit()
def update_videos(new_name,new_time,vid_id):
    cursor.execute("UPDATE videos SET name = ?,time = ? WHERE id = ?" ,(new_name,new_time ,vid_id))
    con.commit()
       
def delete_videos(vid_id):
    cursor.execute("DELETE FROM videos where id = ?",(vid_id,) )
    con.commit()
def main():
    while True:
        
    
        print("\n Youtube Manager app with DB")
        print("1. List Videos")
        print("2.Add videos")
        print("3.Update Videos")
        print("4. Delete Videos")
        print("5.Exit app")
        choice = input("Enter Your Choice : ")
        
        if choice == '1':
            list_videos()
        
        elif choice =='2':
            name = input("Enter the video name:  ")
            time = input("Enter the  video time:  ")
            add_videos(name , time)
            
        elif choice =='3':
            vid_id = input("Enter video_ID you want to update: ")
            name = input("Enter video name: ")
            time = input("Enter video time:  ")
            vid__ = update_videos(name,time,vid_id)
            print(vid__)
        
            
        elif choice == '4':
            vid_id = input("Enter video_ID to delete:  ")
            delete_videos(vid_id)
        elif choice == '5':
            break
        else:
            print("Invalid Choice")
            
    con.close()
if __name__ == "__main__":
    main()


