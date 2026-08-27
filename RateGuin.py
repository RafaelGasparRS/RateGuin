from tabulate import tabulate
import cowsay
import csv
import sys
import os
from datetime import datetime



#art type:  name and format

book = "books.csv"
movie = "movies.csv"
game = "games.csv"


# create class Art (id, name, rate, date, review, favorite[T or F])

class CancelFunction(Exception):
    pass

class Art:

    def __init__(self):
        self._name = ""
        self._rate = 0.0
        self._date = ""
        self._review = ""
        self._favorite = ""

        self.prompts = {
                    "Rate": "What score do you give it (0 to 10)? ",
                    "Date": "When did you finish it (YYYY-MM-DD)? ",
                    "Review": "Write a short review: ",
                    "Favorite": "Is it a favorite of yours (Yes/No)? "
                }

    # NAME
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Please enter a title.")

        self._name = str(name).strip().title()

    # RATE
    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, rate):
        if not rate:
            raise ValueError("Please rate this title.")

        try:
            if "," in rate:
                rate = str(rate).replace(",", ".")
            rate = float(rate)

            if not (0 <= rate <= 10):
                raise ValueError("Please rate it from 0 to 10.")

            self._rate = rate
        except ValueError:
            raise ValueError("Please rate it with a number from 0 to 10.")

    # DATE
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        try:
            datetime.strptime(date, r"%Y-%m-%d")
            self._date = date

        except ValueError:
            raise ValueError ("Invalid date. Use the format YYYY-MM-DD")

    # REVIEW
    @property
    def review(self):
        return self._review

    @review.setter
    def review(self, review):
        self._review = str(review).strip()

    # FAVORITE
    @property
    def favorite(self):
        return self._favorite

    @favorite.setter
    def favorite(self, favorite):
        try:
            favorite = str(favorite).strip().lower()

            if favorite in ['yes', 'y', 't', 'true']:
                self._favorite = "Yes"

            elif favorite in ['no', 'n', 'f', 'false']:
                self._favorite = "No"

            else:
                raise ValueError

        except ValueError():
            raise ValueError("Please enter Yes or No to indicate if this is a favorite.")


# create subclass Book (pages, author)


class Book(Art):
    def __init__(self):
        super().__init__()
        self._pages = ""
        self._author = ""

        self.prompts["Name"] = "What is the title of the book? "
        self.prompts["Pages"] = "How many pages does it have? "
        self.prompts["Author"] = "Who is the author? "

    # PAGES
    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, pages):
        if not pages or str(pages).strip() == "":
            self._pages = ""

        elif not str(pages).isdigit():
            raise ValueError ("Enter an integer number of pages")

        else:
            self._pages = pages

    # AUTHOR
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        self._author = str(author).strip().title()


# create subclass Movie (duration, director)


class Movie(Art):
    def __init__(self):
        super().__init__()
        self._duration = ""
        self._director = ""

        self.prompts["Name"] = "What is the name of the movie/series? "
        self.prompts["Duration"] = "What is the duration in minutes? "
        self.prompts["Director"] = "Who is the director/ creator? "

    # DURATION
    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, duration):
        if not duration or str(duration).strip() == "":
            self._duration = ""
        if not str(duration).isdigit():
            raise ValueError("Please enter the number of minutes.")
        self._duration = f"{int(duration)}"

    # DIRECTOR
    @property
    def director(self):
        return self._director

    @director.setter
    def director(self, director):
        self._director = str(director).strip().title()

# create subclass Game (hours_played, platform, studio)


class Game(Art):
    def __init__(self):
        super().__init__()
        self._hours_played = ""
        self._platform = ""
        self._studio = ""

        self.prompts["Name"] = "What is the name of the game? "
        self.prompts["Hours Played"] = "How many hours did you play? "
        self.prompts["Platform"] = "Which platform did you play on (PS5, PC, SWITCH)? "
        self.prompts["Studio"] = "Which studio made the game? "

    # HOURS PLAYED
    @property
    def hours_played(self):
        return self._hours_played

    @hours_played.setter
    def hours_played(self, hours_played):
        if not hours_played or str(hours_played).strip() == "":
            self._hours_played = ""

        try:

            if "," in hours_played:
                hours_played = str(hours_played).replace(",", ".")

            float(hours_played)
            self._hours_played = hours_played

        except ValueError:
            raise ValueError("Please enter the approximate number of hours played.")





    # PLATFORM
    @property
    def platform(self):
        return self._platform

    @platform.setter
    def platform (self, platform):

        platform = str(platform).lower().strip()
        if platform not in ['ps5', 'pc', 'switch']:
            raise ValueError("Please enter a valid plaftorm (PS5, PC, SWITCH)")

        self._platform = platform.strip().upper()

    # STUDIO
    @property
    def studio(self):
        return self._studio

    @studio.setter
    def studio(self, studio):
        self._studio = str(studio).strip().title()

class Menu:

    main_menu = [
        ["Rate a Book"],
        ["Rate a Movie/Series"],
        ["Rate a Game"],
        ["Help"],
        ["Quit"],
    ]

    index = range(1, len(main_menu) + 1)

    m_menu = tabulate(
        main_menu,
        headers=["Options", "What would you like to do?"],
        showindex=index,
        tablefmt="rounded_grid",
        colglobalalign="center",
    )


    _sub_menu = [["Command:", "home", "add", "edit", "del", "sort", "filter", "quit"]]

    s_menu = tabulate(
        _sub_menu,
        headers=[
            "Options:",
            "Main Menu",
            "Add Item",
            "Edit Item",
            "Delete Item",
            "Sort list",
            "Filter list",
            "Quit",
        ],
        tablefmt="rounded_grid",
        colglobalalign="center",
    )


    def welcome(self):
        clear()
        cowsay.tux("Welcome to - RateGuin -")

    @classmethod
    def start(cls):



        print(cls.m_menu)

        while True:
            try:
                opt = int(input("Provide Command: "))
            except ValueError:
                print("Enter a valid number")
                continue

            if opt == 1:
                clear()
                Functions.show_list(book)
                cls.sub_menu(book)

            elif opt == 2:
                clear()
                Functions.show_list(movie)
                cls.sub_menu(movie)

            elif opt == 3:
                clear()
                Functions.show_list(game)
                cls.sub_menu(game)

            elif opt == 4:
                clear()
                cowsay.tux("Just enter a number corresponding to what you'd  like to do!")
                print(cls.m_menu)

            elif opt == 5:
                clear()
                sys.exit(cowsay.tux("Goodbye!"))

            else:
                clear()
                cowsay.tux("Invalid option. Please choose from 1 to 5.")
                print(cls.m_menu)

    @classmethod
    def sub_menu(cls, art_type):

        print(cls.s_menu)

        while True:

            opts = ["home", "add", "edit", "del", "sort", "filter", "quit"]

            try:
                opt = str(input("Provide Command: ")).strip().lower()
                if opt not in opts:
                    raise ValueError("Enter a valid command")

            except ValueError:
                print("Enter a valid command.\n")
                continue

            #TERMINAR DE PROGRAMAR O SUBMENU

            if opt == "home":
                clear()
                print(cls.m_menu)
                break

            elif opt == "add":
                Functions.add(art_type)
                clear()
                Functions.show_list(art_type)
                print(cls.s_menu)

            elif opt == "edit":
                Functions.edit(art_type)
                clear()
                Functions.show_list(art_type)
                print(cls.s_menu)

            elif opt == "del":
                Functions.delete(art_type)
                clear()
                Functions.show_list(art_type)
                print(cls.s_menu)

            elif opt == "sort":
                Functions.sort_list(art_type)
                print(cls.s_menu)

            elif opt == "filter":
                Functions.filter_list(art_type)
                print(cls.s_menu)

            elif opt == "quit":
                clear()
                sys.exit(cowsay.tux("Goodbye!"))

            else:
                continue


class Functions:

    files_headers = {
        "Book": {
            "file": book,
            "headers": ["Name", "Rate", "Date", "Review", "Favorite", "Pages", "Author"]},
        "Movie": {
            "file": movie,
            "headers": ["Name", "Rate", "Date", "Review", "Favorite","Duration", "Director",]},
        "Game": {
            "file": game,
            "headers": ["Name", "Rate", "Date", "Review", "Favorite", "Hours Played", "Platform", "Studio"]},
    }

    def __init__(self):

        self._init_files()

    @classmethod
    def _init_files(cls):

        for create in cls.files_headers.values():
            if not os.path.exists(create["file"]):
                with open(
                    create["file"], mode="w", newline="", encoding="utf-8"
                ) as file:
                    writer = csv.DictWriter(file, fieldnames=create["headers"])
                    writer.writeheader()

    @classmethod
    def _print_table(cls, rows):
        if not rows:
            clear()
            cowsay.tux("Oops! This list is empty!")

        else:
            index_col = []
            for index, row in enumerate(rows, start=1):
                new_col = {"ID": index}
                new_col.update(row)
                index_col.append(new_col)

            print(
                tabulate(
                    index_col,
                    headers="keys",
                    tablefmt="rounded_grid",
                    colglobalalign="center",
                )
            )

    @classmethod
    def show_list(cls, art_type):
        with open(art_type, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            rows = list(reader)

            cls._print_table(rows)


    @classmethod
    def validate(cls, item, field):

            while True:

                text = item.prompts.get(field, f"{field}: ")
                val = input(text).strip()

                if val.lower() in ["cancel", "quit", "back"]:
                    raise CancelFunction()

                try:

                    # Art
                    if field == "Name":
                        item.name = val
                        return item.name
                    elif field == "Rate":
                        item.rate = val
                        return item.rate
                    elif field == "Date":
                        item.date = val
                        return item.date
                    elif field == "Review":
                        item.review = val
                        return item.review
                    elif field == "Favorite":
                        item.favorite = val
                        return item.favorite

                    # Book
                    elif field == "Pages":
                        item.pages = val
                        return item.pages
                    elif field == "Author":
                        item.author = val
                        return item.author

                    # Movie
                    elif field == "Duration":
                        item.duration = val
                        return item.duration
                    elif field == "Director":
                        item.director = val
                        return item.director

                    # Game
                    elif field == "Hours Played":
                        item.hours_played = val
                        return item.hours_played
                    elif field == "Platform":
                        item.platform = val
                        return item.platform
                    elif field == "Studio":
                        item.studio = val
                        return item.studio

                except ValueError as e:

                    print(f"  -> Error: {e}\n")


    @classmethod
    def add(cls, art_type):

        print("-> Enter 'cancel' to stop this action.")
        art = get_art_type(art_type, Functions.files_headers)

        headers = cls.files_headers[art]["headers"]
        data = {}

        item = make_item(art)

        try:
            for field in headers:
                data[field] = cls.validate(item, field)
        except CancelFunction:
            print("Operation cancelled. No changes were made.")
            return

        with open(art_type, "a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writerow(data)



    @classmethod
    def edit(cls, art_type):



        art = get_art_type(art_type, Functions.files_headers)

        headers = cls.files_headers[art]["headers"]

        item = make_item(art)

        with open(art_type, mode="r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            rows = list(reader)


        if not rows:
            clear()
            cowsay.tux("Oops! This list is empty.")
            return

        clear()

        cls._print_table(rows)
        print(Menu.s_menu)
        print("-> Enter 'cancel' after you choose the column to stop this action.")

        try:
            while True:
                try:
                    idx = int(input("Enter the ID for the title you'de like to edit: ")) -1
                    if not (0 <= idx < len(rows)):
                        raise ValueError ("Invalid ID. Please enter one of the IDs listed above.\n")

                    print(f"Editting {rows[idx]['Name']}...")

                except ValueError as e:
                    print(f" -> Error: {e}")
                    continue


                try:
                    field = input(f"Enter the column you'd like to edit: \n Options: {headers}\n Column: ").strip().title()
                    if not field in headers:
                        raise ValueError("Please enter an existing column.")

                    edit = cls.validate(item, field)
                    rows[idx][field] = edit

                except ValueError as e:
                    print(f" -> Error: {e}")
                    continue

                break

        except CancelFunction:
            print("Operation cancelled. No changes were made.\n")
            return


        with open(art_type, "w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(rows)


    @classmethod
    def delete (cls, art_type):

        with open (art_type, "r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            header = reader.fieldnames

        while True:

            if not rows:
                clear()
                cowsay.tux("Oops! This list is already empty.")
                return

            try:
                idx = int(input("Enter the ID for the title you'de like to delete: ")) -1
                if not (0 <= idx < len(rows)):
                    raise ValueError ("Invalid ID. Please enter one of the IDs listed above.\n")

            except ValueError as e:
                print(f" -> Error: {e}")
                continue

            try:
                prompt = input(f"Would you like to delete {rows[idx]['Name']} (Yes/No)?").lower().strip()

                if not prompt in ['yes', 'y', 'n', 'no']:
                    raise ValueError("Invalid input. Please, enter Yes or No.")

                elif prompt in ['yes', 'y']:
                    print(f"Deleting {rows[idx]['Name']}...")
                    rows.pop(idx)

                elif prompt in ['no', 'n']:
                    return print(f"{rows[idx]['Name']} was not deleted.")

            except ValueError as e:
                print(f" -> Error: {e}")
                continue

            break

        with open(art_type, "w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()
            writer.writerows(rows)

    @classmethod
    def sort_list(cls, art_type):

        art = get_art_type(art_type, cls.files_headers)
        headers = cls.files_headers[art]["headers"]
        headers = [h for h in headers if h not in ['Review', 'Studio']]


        while True:
            try:
                key = input(f"Order by which column?\n Options: {headers}\n").strip().title()
                if key not in headers:
                    raise ValueError("Invalid Column. Choose one of the options given.")
            except ValueError as e:
                print(f"  -> Error: {e}\n")
                continue
            try:
                reverse = input("Would you like to invert the order? (Yes/No)").lower()
                if reverse in ['yes', 'y', 't', 'true']:
                    reverse = True

                elif reverse in ['no', 'n', 'f', 'false']:
                    reverse = False

                else:
                    raise ValueError("Invalid entry.")
            except ValueError as e:
                print(f"-> Error: {e}")
                continue

            break

        with open(art_type, "r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            rows = list(reader)

        if key == "Rate":
            rows = sorted(rows, key=lambda rows: float(rows[key]), reverse=reverse)

        else:

            rows = sorted(rows, key=lambda rows: rows[key], reverse=reverse)

        clear()
        cls._print_table(rows)

    @classmethod
    def filter_list(cls, art_type):

        art = get_art_type(art_type, cls.files_headers)
        headers = cls.files_headers[art]["headers"]
        headers = [h for h in headers if h not in ['Review']]

        while True:
            try:
                column = input(f"Filter by which column? \n Options: {headers}\n").strip().title()
                if column not in headers:
                    raise ValueError("Enter a valid column.")
            except ValueError as e:
                print (f"-> Error: {e}")
                continue

            break

        value = input(f"Show {art} where {column} is: ").strip()

        with open(art_type, "r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            rows = list(reader)

        matches = [row for row in rows if row[column].lower() == value.lower()]
        clear()
        cls._print_table(matches)


 # Gets the art type and returns to the add and edit functions

def get_art_type(art_type, files_headers):
    for key, value in files_headers.items():
        if value["file"] == art_type:
            return key
    return None

 # Creates the object for the add and edit functions

def make_item(art):
    if art == "Book":
        return Book()
    elif art == "Movie":
        return Movie()
    elif art == "Game":
        return Game()

    return None

 # Clears the terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    menu = Menu()
    fun = Functions()
    menu.welcome()
    menu.start()


if __name__ == "__main__":
    main()
