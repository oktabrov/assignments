from dataclasses import dataclass, field
class TrackError(Exception):
    pass

@dataclass
class Track:
    code: str
    title: str
    genre: str
    duration: int
    _status: str = field(init=False, default="PENDING")
    def __post_init__(self):
        if self.duration <= 0:
            raise TrackError(f"Invalid duration for {self.code}")
    @property
    def minutes(self):
        return round(self.duration / 60, 1)
    def __str__(self):
        return f"[{self.code}] {self.title} ({self.genre}, {self.duration}s) -> {self._status}"
    def __gt__(self, other: "Track"):
        if not isinstance(other, Track):
            return NotImplemented
        return self.duration > other.duration

class PlaylistFilter:
    def __init__(self, tracks, genres):
        self._tracks = tracks
        self._genres = set(genres)
        self._cursor = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self._cursor >= len(self._tracks):
            raise StopIteration
        track = self._tracks[self._cursor]
        self._cursor += 1

        if track.genre in self._genres:
            track._status = "QUEUED"
        else:
            track._status = "SKIPPED"
        return track

def playlist_report(filt):
    queued = 0
    skipped = 0
    for track in filt:
        if track._status == "QUEUED":
            queued += 1
        else:
            skipped += 1
        yield str(track)
    yield f"Summary: {queued} queued, {skipped} skipped"

class PlaylistSession:
    def __init__(self, name):
        self.name = name
        self._tracks = []
    def __enter__(self):
        print(f"=== Playing: {self.name} ===")
        return self
    def add(self, track):
        self._tracks.append(track)
    def filter(self, genres):
        filt = PlaylistFilter(self._tracks, genres)
        return playlist_report(filt)
    def __exit__(self, exc_type, exc, tb):
        if exc_type is not None and exc_type == TrackError:
            print(f"!!! Error: {exc}")
            print(f"=== Stopped: {self.name} ({len(self._tracks)} tracks) ===")
            return True
        print(f"=== Stopped: {self.name} ({len(self._tracks)} tracks) ===")
        return False
with PlaylistSession("Road Trip") as pl:
    pl.add(Track("T01", "Bohemian Rhapsody", "Rock", 354))
    pl.add(Track("T02", "Blinding Lights", "Pop", 200))
    pl.add(Track("T03", "Clair de Lune", "Classical", 330))

    for line in pl.filter(("Rock", "Pop")):
        print(line)

    print(pl._tracks[0] > pl._tracks[1])

print()

with PlaylistSession("Study Session") as pl:
    pl.add(Track("T04", "White Noise", "Ambient", -60))
