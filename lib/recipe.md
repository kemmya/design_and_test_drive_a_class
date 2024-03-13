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
        pass 

    def add(self, track):
        # Parameters: track string
        #   track: string representing a single track
        # Returns:
        #   Nothing
        pass 

    def all_tracks(self):
        # Returns:
        #  List of instances of tracks user listen to
        pass # No code here yet
    def search_by_heading(self, heading):
        # Parameter: topic string
        # side effect: search the heading of all tracks
        # Return => List of tracks with heading
        pass
    ```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python




"""
all tracks  user listens to
Returns all the tracks
"""
music_library = MusicLibrary()
music_library.add("Let her go")
music_library.add("Survivors")
music_library.add("Holes")
music_libray.all_tracks() #  => ["Let her go", "Survivors", "Holes"]  

""" 
When i search track by heading to 
Return all tracks user listens to
"""
music_library = MusicLibrary()
music_library.add("Let her go")
music_library.add("Survivors")
music_library.add("Holes") 
music_library.search_by_title("Let her go", "Survivors", "Holes") #=> ["Let her go", "Survivors", "Holes"]

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

``` python


"""
when i add multiple tracks to list of music
User listen to
"""
def test_add_multiple_tracks_to_list_of_music():

"""
when all tracks are searched by the heading
"""
def test_search_by_title():
