from lib.diary_entry import *

"""
given a title and contents, the method instantiates and returns a formatted diary entry
"""
def test_formats_title_and_contents():
    diary_entry = DiaryEntry("Friday", "Counting Challenge")
    result = diary_entry.format()
    assert result == "Friday: Counting Challenge"

"""
given a title and contents, it can count the words in the diary entry 
"""
def test_counts_words_in_diary_entry(): 
    diary_entry = DiaryEntry("Friday", "Counting Challenge One Two Three Four")
    result = diary_entry.count_words()
    assert result == 7

"""
given contents and wpm, it can calculate the reading time
e.g reading 1 word per minute, it would take 3 mins to read "Friday, Counting Challenge"
"""
def test_calculate_reading_time_of_contents():
    diary_entry = DiaryEntry("Friday", "Counting Challenge One Two Three Four")
    result = diary_entry.reading_time(2)
    assert result == 3

"""
given minutes reader has, it will return the chunk of text that can be read
e.g. with 6 words and, 2 wpm, and 2 minutes, return first two words
"""
def test_generate_text_which_can_be_read_in_two_minutes():
    diary_entry = DiaryEntry("Friday", "Counting Challenge One Two Three Four")
    result = diary_entry.reading_chunk(2,2)
    assert result == "Counting Challenge One Two"

"""
given more minutes, it will return the next chunk of text
e.g.    first time "Counting Challenge One Two"
        second time "Three Four Five Six"
"""
def test_generate_text_which_can_be_read_called_twice():
    diary_entry = DiaryEntry("Friday", "Counting Challenge One Two Three Four Five Six Seven Eight Nine Ten")
    assert diary_entry.reading_chunk(2,2) == "Counting Challenge One Two"
    assert diary_entry.reading_chunk(2,2) == "Three Four Five Six"
    assert diary_entry.reading_chunk(2,2) == "Seven Eight Nine Ten"