class song:
    def __init__(self,name):
        self.name=name
        self.next=None
class playlist:
    def __init__(self):
        self.head=None
    def add_song(self,song_name):
        new_song=song(song_name)
        if self.head is None:
            self.head = new_song
        else:
            temp = self.head
            while temp.next:
                temp=temp.next
            temp.next=new_song
        print(song_name,"added a playlist")
playlist = playlist()
print("\n----MUSIC PLAYLIST----")
print("1:create a playlist")
print("2.add a new list")
print("3delete a song")
print("4display playlist")
print("5exit")


choice = int(input("enter your choise"))

if choice ==1:
    music=input("enter song name:")
    playlist.add_song(music)
    


    

