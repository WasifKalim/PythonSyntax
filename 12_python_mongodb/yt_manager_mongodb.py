# Most things in mongodb goes in curly bracket 

# import pymongo
from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb+srv://wasif114222:81err3oqWIF4J44e@cluster0.p1utm.mongodb.net/python?retryWrites=true&w=majority&appName=Cluster0")

db = client["ytmanager"] # collection name
video_collection = db["videos"] # table name

print(video_collection)

def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})

def list_videos():
    for video in video_collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']}, Time: {video['time']}")

def update_video(video_id, name, time):

    video_collection.update_one(
        {'_id': ObjectId(video_id)},
        {"$set": {"name": name, "time": time}}
    )

def delete_video(video_id):
    video_collection.delete_one({'_id':ObjectId(video_id)})


def main():
    while True:
        print("\n Youtube manager App")
        print("1. List all videos ")
        print("2. Addd a new videos")
        print("3. Update a videos")
        print("4. Delete a video")
        print("5. Exit the app")

        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name, time)
        elif choice == '3':
            video_id = input("Enter the video id to update: ")
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            update_video(video_id, name, time)
        elif choice == '4':
            video_id = input("Enter the video id to delete: ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Enter valid input")

if __name__ == "__main__":
    main()
