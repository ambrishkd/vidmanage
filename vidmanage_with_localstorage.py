import json

def load_data():
    try:
        with open("videos.txt", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_data_helper(videos):
    with open("videos.txt", "w") as file:
        json.dump(videos, file)


def list_all_videos(videos):
    print('\n')
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']} - {video['time']}")


def add_a_video(videos):
    name = input("Enter the Video Title: ")
    time = input("Enter the Video Time: ")
    videos.append({"name": name, "time": time})
    save_data_helper(videos)


def update_a_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the index of the video to update: "))
    if 1 <= index <= len(videos):
        name = input("Enter the new Video Title: ")
        time = input("Enter the new Video Time: ")
        videos[index-1] = {"name": name, "time": time}
        save_data_helper(videos)
    else:
        print("Invalid Index")


def delete_a_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the index of the video to delete: "))
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid Index")


def main():
    videos = load_data()
    while True:
        print("\nVidmanage | Choose an Option")
        print("1. List all YouTube Videos")
        print("2. Add a YouTube Video")
        print("3. Update a YouTube Video")
        print("4. Delete a YouTube Video")
        print("5. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_a_video(videos)
            case "3":
                update_a_video(videos)
            case "4":
                delete_a_video(videos)
            case "5":
                break   
            case _:
                print("Invalid Choice")


if __name__ == "__main__":
    main()