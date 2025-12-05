class DiaryEntry():
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.read_so_far = 0

    def format(self):
        return f"{self.title}: {self.contents}"
    
    def count_words(self):
        title_count = len((self.title).split())
        content_count = len((self.contents).split())
        word_count = title_count + content_count
        return word_count 
    
    def reading_time(self, wpm):
        self.wpm = wpm
        content_count = len((self.contents).split())
        return content_count / self.wpm

    def reading_chunk(self, wpm, minutes):
        words = self.contents.split()
        words_can_read = int(wpm * minutes)

        chunk_start = self.read_so_far
        chunk_end = self.read_so_far + words_can_read
        # content_now = " ".join(words[:words_can_read])
        content_now = words[chunk_start:chunk_end]
        self.read_so_far = words_can_read
        return " ".join(content_now)
        # can't quite get this last bit to work. 