import csv
from pathlib import Path


def read_file(file_name: str):
    filename = Path("static", "fixtures", file_name)
    with open(filename, mode="r", encoding="utf8") as file:
        reader = csv.DictReader(file, delimiter=";")
        datasets = list(reader)
    return datasets


def get_cities_datasets() -> list[dict]:
    return read_file(file_name="cities.csv")


def get_grades_datasets() -> list[dict]:
    return read_file(file_name="grades.csv")


def get_jobs_datasets() -> list[dict]:
    return read_file(file_name="jobs.csv")


def get_themes_datasets() -> list[dict]:
    return read_file(file_name="themes.csv")


def get_tools_datasets() -> list[dict]:
    return read_file(file_name="tools.csv")


def get_event_types_datasets() -> list[dict]:
    return read_file(file_name="event_types.csv")
