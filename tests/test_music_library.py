from lib.music_library import *

"""
when i add multiple tracks to list of music
User listen to
"""
def test_add_multiple_tracks_to_list_of_music():
    music_library = MusicLibrary()
    music_library.add("Let her go")
    music_library.add("Survivors")
    music_library.add("Holes")
    assert music_library.all_tracks() == ["Let her go", "Survivors", "Holes"]  

"""
when all tracks are searched by the heading
"""
def test_search_by_title():
    music_library = MusicLibrary()
    music_library.add("Let her go")
    music_library.add("Survivors")
    music_library.add("Holes") 
    assert music_library.search_by_title("Let her go" "Survivors" "Holes") == ["Let her go", "Survivors", "Holes"]




