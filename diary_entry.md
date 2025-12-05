``` Python
Purpose 
-- User can format a title and contents into a diary entry
-- User can see the number of words in the diary entry 
-- The program can work out the the reading time for the diary entry, using readers words per minute
-- If the reader inputs the number of minutes they have to read, the program will calculate and return an appropraite chunk of text
using the readers wpm. 

class DiaryEntry():
def __init__(self, title, contents): 
    """ Method 1, the method can initiate an object
    Parameters: title - a string , and contents - a string
    Returns: none
    Side effects: none
    """ 

def format(self):
    """ Method 2, the method can format title and contents
    Parameters: none
    Returns: a formatted string from title and contents: "My Title: These are the contents"
    Side effects: none? are we creating and storing the 'diary entry'? 
    """

def count_words(self):
    """ Method 3, the method can count words in the title and contents
    Parameters: none
    Returns: an integer, the word count of the contents
    Side effects: stores the word count?
    """

def reading_time(self, wpm):
    """ Method 4, the method can calculate reading time from word count and wpm.
    Parameters: wpm
    Returns: an integer, the number of minutes it will take to read the contents 
    Side effects: None
    """

def reading_chunk(self, wpm, minutes):
    """ Method 5, the method can calculate amount of text that can be read in time given
    and present this to the reader.  If more time is allocated, the next chunk will be 
    calculated, until the whole contents has been read. 
    Parameters: wpm - integer, and minutes - integer
    returns: string, next chunk of text that can be read. 
    """

```