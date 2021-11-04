def cardinals(n):
    # this function takes an integer and returns it's cardinal (1 --> 1st, 2 --> 2nd, 3 --> 3rd etc)
    if n % 100 == 11 or n % 100 == 12 or n % 100 == 13:
        cardinal = str(n) + "th"
        return cardinal

    if n % 10 == 1:
        cardinal = str(n) + "st"
        return cardinal
    elif n % 10 == 2:
        cardinal = str(n) + "nd"
        return cardinal
    elif n % 10 == 3:
        cardinal = str(n) + "rd"
        return cardinal
    else:
        cardinal = str(n) + "th"
        return cardinal
