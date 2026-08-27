import pytest
from project import get_art_type, make_item
from project import Art, Book, Movie, Game, Functions

def test_valid_name():
    art = Art()
    art.name = "dune"
    assert art.name == "Dune"


def test_name_exists():
    art = Art()
    with pytest.raises(ValueError):
        art.name = ""


def test_rate_exists():
    art = Art()
    with pytest.raises(ValueError):
        art.rate =""


def test_rate_0to10():
    art = Art()
    with pytest.raises(ValueError):
        art.rate = "15"
        art.rate = "-10"


def test_get_art_type():
    assert get_art_type("books.csv", Functions.files_headers) == "Book"
    assert get_art_type("games.csv", Functions.files_headers) == "Game"
    assert get_art_type("movies.csv", Functions.files_headers) == "Movie"


def test_get_art_type_invalid():
    assert get_art_type("nada.csv", Functions.files_headers) is None


def test_make_item():
    assert isinstance(make_item("Book"), Book)
    assert isinstance(make_item("Movie"), Movie)
    assert isinstance(make_item("Game"), Game)


def test_make_item_invalid():
    assert make_item("nada") is None

