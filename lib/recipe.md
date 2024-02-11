# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.



## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python


class MusicLibrary:
    def __init__(self):
        # Parameters: => None
        #   Returns => Nothing
        # Side effects: Empty list in new variable track
        pass # No code here yet

    def add(self, track):
        # Parameters: track string
        #   task: string representing a single track
        # Returns:
        #   string track to music list
        pass # No code here yet

    def all_tracks(self):
        # Returns:
        #  List of all tracks user listen to
        pass # No code here yet
    def search_by_heading(self, heading):
        # Parameter: topic string
        # Return => List of tracks with heading
        pass
    ```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python


"""
Initially no track was given
"""
music_library = MusicLibrary()
music_library.track() # => []

"""
Add one track to list of music
User listen to
"""
music_library = MusicLibrary
music_library.add("Let her go") # => [Let her go"]

"""
all tracks  user listens to
Returns all the tracks
"""
music_library = MusicLibrary
music_library.add("Let her go")
music_library.add("Survivors")
music_library.add("Holes")
music_libray.all_tracks() #  => ["Let her go" "Survivors" "When we were young"]  

""" 
When i search track by heading to 
Return all tracks user listens to
"""
music_library = MusicLibrary
music_library.add("Let her go") 
music_library.add("Survivors")
music_library.add("Holes")
music_library.search_by_heading() # => [] -returns list of all tracks by heading
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

``` python

"""
When initially no track was given
"""
def test_initially_no_track_given():

"""
when i add one track to list of music
User listen to
"""
def test_add_one_track_to_list_of_music():

"""
When all tracks are added
Returns all the tracks
"""
def test_all_tracks_in_music_list():

""" 
When i search track by heading to 
Return all tracks user listens to
"""
def test_search_track_by_heading():
