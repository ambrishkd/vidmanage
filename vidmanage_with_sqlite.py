import sqlite3

conn = sqlite3.connect('videos.db')
cur = conn.cursor()
cur.execute('''
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
''')


def list_all_videos():
    cur.execute("SELECT * FROM videos")
    result = cur.fetchall()
    if not result:
        print("No Videos Found!")
        return
    for row in result:
        print(f"{row[0]}. {row[1]} - {row[2]}")


def add_a_video(name, time):
    cur.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()


def update_a_video(name, time, index):
    cur.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (name, time, index))
    conn.commit()


def delete_a_video(index):
    list_all_videos()
    cur.execute("DELETE FROM videos WHERE id = ?", (index,))
    conn.commit()


def main():
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
                list_all_videos()
            case "2":
                name = input("Enter the Video Title: ")
                time = input("Enter the Video Time: ")
                add_a_video(name, time)
            case "3":
                list_all_videos()
                index = int(input("Enter the index of the video to update: "))
                name = input("Enter the new Video Title: ")
                time = input("Enter the new Video Time: ")
                update_a_video(name, time, index)
            case "4":
                list_all_videos()
                index = int(input("Enter the index of the video to delete: "))
                delete_a_video(index)
            case "5":
                break   
            case _:
                print("Invalid Choice")
    conn.close()


if __name__ == '__main__':
    main()