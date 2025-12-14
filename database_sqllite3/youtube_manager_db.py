import sqlite3

conn = sqlite3.connect('youtube_videos.db')

cursor = conn.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS videos (
                   id INTEGER PRIMARY KEY, 
                   name TEXT NOT NULL, 
                   description TEXT NOT NULL
               )
               
               ''')




def list_all_videos():
    list_of_videos= cursor.execute("SELECT * FROM videos").fetchall()
    for video in list_of_videos:
        print(f"ID: {video[0]}, Name: {video[1]}, Description: {video[2]}")
    
    

def upload_video(conn, cursor, video_name, video_description):
    cursor.execute(
        'INSERT INTO videos (name, "description") VALUES (?, ?)',
        (video_name, video_description)
    )
    conn.commit()

def update_video(video_id, video_new_name, video_new_description):
    cursor.execute('UPDATE videos SET name = ? , description = ? where id = ?', (video_new_name,video_new_description,video_id))
    conn.commit()

def delete_video(video_id):
    cursor.execute('DELETE FROM videos WHERE id = ? ', (video_id,))
    conn.commit()


def main():


    while True: 

        print("\n Youtube Manager | Choose an option:")
        print("1. List all videos")
        print("2. Upload a video")
        print("3. Update video details")
        print("4. Delete a video")
        print("5. Exit")


        choice = input("Enter your choice (1-5): ")

        match choice:
            case '1':                
                list_all_videos()
            case '2':
                name= input("Enter the video name: ")
                description= input("Enter the video description: ")
                
                upload_video(video_name=name,video_description= description)
            case '3':
                video_id= input("Enter the id of the video: ")
                name= input("Enter the video new name: ")
                description= input("Enter the video new description:")
                
                update_video(video_id=video_id,video_new_name=name,video_new_description=description)
                
            case '4':
                video_id= input("Enter the id of the video: ")
                delete_video(video_id)
            case '5':
                print("Exiting Youtube Manager. Goodbye!")
                break
            case _:
                print("Invalid choice. Please enter a number between 1 and 5.")

    conn.close()




if __name__ == "__main__" :
    
    main()
