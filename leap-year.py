def is_leap(year):
    leap = False
    points = 0
    # write your logic here
    if (year % 100 != 0):
        points += 1
    if (year % 400 == 0):
        points += 1
    if (year % 4 == 0):
        points += 1

    if points == 2:
        leap = True
    else:
        leap = False
    print(f'year: {year}, points: {points}')
    return leap

years = [1990, 2000, 2012, 2004, 2400, 1800, 1900, 2100, 2200, 2300, 2500]

for year in years:
    print(is_leap(year))