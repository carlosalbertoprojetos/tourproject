import datetime

currentDateTime = datetime.datetime.now()
date = currentDateTime.date()


def years_select():
    years_list = []
    currently_year = date.strftime("%Y")
    years_list.append(currently_year)
    year_number = int(currently_year)
    for i in range(8):
        year_number += 1
        years_list.append(year_number)


    return years_list
