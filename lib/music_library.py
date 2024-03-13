class MusicLibrary:
    def __init__(self):
        self._tracks = []

    def add(self, track):
        self._tracks.append(track)

    def all_tracks(self):
        return self._tracks

    def search_by_title(self, heading):
        return [track for track in self._tracks if heading in track.title]