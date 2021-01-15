#!/usr/bin/env python3

from datetime import date
import subprocess
import utils


if __name__ == "__main__":
    today = date.today()
    today_s = (
        f"{utils.week_days[today.weekday()]} the"
        + f" {today.day}{utils.day_suffix(today.day)}"
        + f" of {utils.months[today.month]}, {today.year} : "
    )
    for zodiac in utils.zodiac_signs:
        prefix = f"{zodiac} Horoscope of "
