As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.


```python
# THE CLASS
class Spotifoo:
    # user facing properties, string name of the song

def __init__(self):
    # Arguements: none
    # side effect:

def add_songs(self, song):
    # parameters, string, name of the song
    # returns nothing 
    # side effect, saves the song to the self object 

def list_songs(self):
    # parameters, none
    # returns, the list of the songs

```
```python 
# THE TESTS

"""
Given a new song
#Task: song gets added to song storage
"""
test_check_song_is_added_to_storage():
    spotifoo = Spotifoo()
    spotifoo.add_songs("song1")
    result = spotifoo.list_songs()
    assert result == ["song1"]

"""
Given a new Spotifoo instance 
#Task: check that the list is empty to begin with
"""
test_check_list_is_empty():
    spotifoo = Spotifoo()
    assert spotifoo.list_songs() == []

"""
Given a new song
#Task: program returns the complete list of songs
"""
test_check_program_returns_list_of_songs():
    spotifoo = Spotifoo()
    spotifoo.add_songs("song1")
    spotifoo.add_songs("song2")
    assert spotifoo.list_songs() == ["song1", "song2"]

# """
# Given an empty string
# #Task: program returns an error message
# """


```
