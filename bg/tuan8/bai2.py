class MP3Player():
    def __init__(self):
        self.music_queue = []
        self.current_song = "Example_1"
        
    def add_song(self):
        song = input("Enter the name of the song: ")
        self.music_queue.append(song)
        
    def play_next_song(self):
        if not self.music_queue:
            print("No song in the queue!")
        else:
            self.current_song = self.music_queue.pop(0) 
            print(f"Now playing: {self.current_song}")
        
    def skip_song(self):
        if len(self.music_queue) < 2: 
            print("Not enough songs to skip!")
        else:
            skipped_song = self.music_queue.pop(0)
            self.current_song = self.music_queue[0] 
            print(f"Skipped: {skipped_song}, now playing: {self.current_song}")

    def run(self):
        while True:
            print(f"Currently playing: {self.current_song}")
            print("1. Add song\n2. Play next song\n3. Skip song\n4. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_song()
            elif choice == "2":
                self.play_next_song()
            elif choice == "3":
                self.skip_song()
            elif choice == "4":
                print("Exit")
                break
            else:
                print("Please choose an option between 1 and 4!")
run_song = MP3Player()
run_song.run()
