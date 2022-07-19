def upcoming_holiday():
    from datetime import date
    import datetime

    print(f'Todays date is {date.today()}')
    Tisha_bav=datetime.datetime(2022,8,6,0,0,0,0)

    time_until_holiday= Tisha_bav-datetime.datetime.now()

    print(f"Tisha B'av is in {time_until_holiday}")


upcoming_holiday()
