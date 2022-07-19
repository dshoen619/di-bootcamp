def time_well_spent():
    from datetime import date
    import datetime
    import time

    birthyear=int(input("Enter your birth year ('yyyy')"))
    birth_month=int(input("Enter your birth month ('mm')"))
    birth_day=int(input("Enter the day you were born ('dd')"))

    current_time= datetime.datetime.now()
    birth_time=datetime.datetime(birthyear,birth_month,birth_day,0,0,0,0)

    time_lived=current_time-birth_time

    print(f"You have lived a wonderful {time_lived.total_seconds()/60} minutes!")

time_well_spent()




