class Song:
    def __init__(self, name):
        self.name = name
        self.next = None


class Playlist:
    def __init__(self):
        self.head = None

   
    def add_song(self, song_name):
        new_song = Song(song_name)
        if self.head is None:
            self.head = new_song
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_song
        print(f"'{song_name}' added to playlist.")

   
    def insert_song(self, position, song_name):
        new_song = Song(song_name)
        if position == 1:
            new_song.next = self.head
            self.head = new_song
            print(f"'{song_name}' inserted at position {position}.")
            return

        temp = self.head
        count = 1
        while temp and count < position - 1:
            temp = temp.next
            count += 1

        if temp is None:
            print("Invalid position!")
        else:
            new_song.next = temp.next
            temp.next = new_song
            print(f"'{song_name}' inserted at position {position}.")

   
    def delete_song(self, song_name):
        temp = self.head

        if temp is not None:
            if temp.name == song_name:
                self.head = temp.next
                print(f"'{song_name}' removed from playlist.")
                return

        prev = None
        while temp is not None:
            if temp.name == song_name:
                break
            prev = temp
            temp = temp.next

        if temp is None:
            print(f"'{song_name}' not found in the playlist.")
            return

        prev.next = temp.next
        print(f"'{song_name}' removed from playlist.")

   
    def display_playlist(self):
        if self.head is None:
            print("Playlist is empty.")
            return

        print("\n--- Current Playlist ---")
        temp = self.head
        position = 1
        while temp:
            print(f"{position}. {temp.name}")
            temp = temp.next
            position += 1
        print("------------------------")



my_playlist = Playlist()

while True:
    print("\n*** MUSIC PLAYLIST MENU ***")
    print("1. Add Song (End of Playlist)")
    print("2. Insert Song at Position")
    print("3. Delete Song by Name")
    print("4. Display Playlist")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Enter song name to add: ")
        my_playlist.add_song(name)
    elif choice == "2":
        pos = int(input("Enter position to insert: "))
        name = input("Enter song name to insert: ")
        my_playlist.insert_song(pos, name)
    elif choice == "3":
        name = input("Enter song name to delete: ")
        my_playlist.delete_song(name)
    elif choice == "4":
        my_playlist.display_playlist()
    elif choice == "5":
        print("Exiting playlist application.")
        break
    else:
        print("Invalid choice! Please select between 1 and 5.")
