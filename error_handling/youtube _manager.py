import json
import time 

def load_data():
    try:
        with open("youtube.txt", "r") as file:
            json_data= json.load(file)
            return json_data


    except FileNotFoundError:
        print("Error: The data file was not found.")
        return []
    except :
        print("Error: An unexpected error occurred while loading data.")
        return []

def save_data_helper(videos):
    try:
        with open("youtube.txt", "w") as file:
            json.dump(videos, file, indent=4)
    except IOError:
        print("Error: Unable to save data to file.")

def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    for index,video in enumerate(videos, start=1):
        print(f"{index}. Title: {video['title']}, Description: {video['description']}")

    print("\n")
    print("*" * 70)
    time.sleep(2)
    
    

def upload_video(videos):
    
    name = input("Enter video title: ")
    description = input("Enter video description: ")
    videos.append({"title": name, "description": description})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to update: "))
    if not (1 <= index <= len(videos)):
        print("Invalid video number.")
        return
    
    new_title = input("Enter the new video title: ")
    new_description = input("Enter the new description: ")

    videos[index - 1]["title"] = new_title
    videos[index - 1]["description"] = new_description
    save_data_helper(videos)
    print("video updated successfully")

def delete_video(videos):
    list_all_videos(videos)
    try:
        deletion_index = int(input("Enter the video number to delete: ")) - 1
    except ValueError:
        print("Please enter a valid number.")
        return

    if not (0 <= deletion_index < len(videos)):
        print("Invalid video number.")
        return

    deleted = videos.pop(deletion_index)
    save_data_helper(videos)
    print(f"Deleted: {deleted['title']}")



def main():


    videos = load_data()
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
                list_all_videos(videos)
            case '2':
                upload_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                print("Exiting Youtube Manager. Goodbye!")
                break
            case _:
                print("Invalid choice. Please enter a number between 1 and 5.")




if __name__ == "__main__":
    main()
    