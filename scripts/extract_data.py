#!/usr/bin/env python3
import sys
from pathlib import Path
from datetime import date
from functools import reduce
from sklearn.model_selection import train_test_split
import pandas as pd
import utils


def date_to_words(d):
    date_list = d.split("-")
    weekday = date.fromisoformat(
        f"{date_list[2]}-{date_list[0]}-{date_list[1]}"
    ).weekday()
    return (
        f"{utils.week_days[weekday]} the {int(date_list[1])}{utils.day_suffix(date_list[1])}"
        + f" of {utils.months[int(date_list[0])]}, {date_list[2]}"
    )


def prefix(d, zodiac):
    return f"<BOS> {zodiac.capitalize()} Horoscope of {date_to_words(d)} : "


def build_dataset(rows, path):
    with open(path, "w") as file:
        file.write(reduce(lambda s1, s2: s1 + s2, rows, ""))


def extract_data(path):
    if path.suffix != ".csv":
        raise ValueError("File should be .csv")

    df = pd.read_csv(str(path), sep="|")
    rows = [
        prefix(values["date"], values["zodiac"])
        + values["horoscope"].strip()
        + " <EOS>"
        + "\n"
        for i, values in df.iterrows()
    ]

    full_train, test = train_test_split(rows, train_size=0.9)
    train, valid = train_test_split(full_train, train_size=7 / 9)

    return train, valid, test


if __name__ == "__main__":
    path = Path(sys.argv[1])
    train, valid, test = extract_data(path)
    build_dataset(train, path.parent / "train.txt")
    build_dataset(valid, path.parent / "valid.txt")
    build_dataset(test, path.parent / "test.txt")
