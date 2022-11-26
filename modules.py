import os
from pathlib import Path


def init():
    os.chdir(Path(__file__).parent)


def get_data_string(name: str):
    return open(f"data/{name}.txt", "r", encoding="utf8").read().splitlines()


def get_data(name: str, type: type):
    return list(map(type, get_data_string(name)))
