from dotenv import load_dotenv
import pymongo 
from bson import ObjectId
from bson.errors import InvalidId
import os

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")  
if not MONGODB_URI:
    raise ValueError("MONGODB_URI not found. Put it in your .env file.")

client = pymongo.MongoClient(MONGODB_URI)
db = client["youtube_manager"]

video_collection = db["videos"]

print(video_collection)





def list_all_videos():
    
    videos_list= video_collection.find()
    for video in videos_list:
        print(f"ID: {video['_id']}, Name: {video['name']}, Description: {video['description']}")
    
    

def upload_video( video_name, video_description):
    video_collection.insert_one({"name":video_name, "description": video_description})




def update_video(video_id, video_new_name, video_new_description):
    try:
        input_id = ObjectId(video_id)        
        video_collection.update_one({"_id": input_id}, {"$set": {"name": video_new_name, "description": video_new_description}})
        
    except InvalidId:
        print("Invalid MongoDB id format.")
        return


def delete_video(video_id):
    try:
        delete_id = ObjectId(video_id)   # ✅ correct
    except InvalidId:
        print("Invalid MongoDB id format.")
        return

    video_collection.delete_one({"_id": delete_id})








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


if __name__== "__main__" :
    main()