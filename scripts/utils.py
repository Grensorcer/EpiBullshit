week_days = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}

months = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}

zodiac_signs = [
    "Aquarius",
    "Virgo",
    "Leo",
    "Scorpio",
    "Sagittarius",
    "Cancer",
    "Aries",
    "Gemini",
    "Taurus",
    "Libra",
    "Capricorn",
    "Pisces",
]


def day_suffix(day):
    mod = int(day) % 10
    if mod == 1 and int(day) != 11:
        res = "st"
    elif mod == 2 and int(day) != 12:
        res = "nd"
    elif mod == 3 and int(day) != 13:
        res = "rd"
    else:
        res = "th"
    return res
