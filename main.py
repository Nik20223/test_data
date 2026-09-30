"""Распределяет книги из books.csv между пользователями из users.json.

На выходе формирует result.json, где у каждого пользователя появляется
массив books с назначенными ему книгами (максимально поровну).
"""

import csv
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
BOOKS_PATH = BASE_DIR / "test-data" / "books.csv"
USERS_PATH = BASE_DIR / "test-data" / "users.json"
RESULT_PATH = BASE_DIR / "result.json"


def read_books(path):
    """Читает книги из CSV в список словарей."""
    with open(path, encoding="utf-8") as file:
        return list(csv.DictReader(file))


def read_users(path):
    """Читает пользователей из JSON в список словарей."""
    with open(path, encoding="utf-8") as file:
        return json.load(file)


def distribute_books(books, users):
    """Раздаёт книги пользователям максимально поровну.

    Первые ``остаток`` пользователей получают на одну книгу больше.
    """
    per_user, remainder = divmod(len(books), len(users))
    start = 0
    for index, user in enumerate(users):
        count = per_user + (1 if index < remainder else 0)
        user["books"] = books[start:start + count]
        start += count
    return users


def main():
    users = read_users(USERS_PATH)
    books = read_books(BOOKS_PATH)
    result = distribute_books(books, users)
    with open(RESULT_PATH, "w", encoding="utf-8") as file:
        json.dump(result, file, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    main()
