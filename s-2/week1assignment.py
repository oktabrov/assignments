class CinemaHall:
    cinema_name = "Silver Screen"
    max_viewers = 5
    total_halls = 0

    def __init__(self, hall_number, movie_title):
        self.hall_number = hall_number
        self.movie_title = movie_title
        self.viewers = []
        CinemaHall.total_halls += 1

    def seat_viewer(self, name):
        if len(self.viewers) < CinemaHall.max_viewers:
            self.viewers.append(name)
            print(f"Seated {name} in Hall {self.hall_number}")
        else:
            print("Hall is full")

    def remove_viewer(self, name):
        if name in self.viewers:
            self.viewers.remove(name)
            print(f"Removed {name} from Hall {self.hall_number}")
        else:
            print("Viewer not found")

    def display_hall(self):
        print(f"Hall {self.hall_number} showing {self.movie_title} at {CinemaHall.cinema_name}")


hall = CinemaHall(3, "Inception")

hall.display_hall()
hall.seat_viewer("Aziz")
hall.seat_viewer("Bobur")
hall.seat_viewer("Charos")
hall.seat_viewer("Dilshod")
hall.seat_viewer("Eldor")
hall.seat_viewer("Feruza")
hall.remove_viewer("Bobur")
hall.remove_viewer("Gulnora")
count = CinemaHall.total_halls
print(f"Total halls: {count}")