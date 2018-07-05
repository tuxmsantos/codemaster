#My Master = Mr.Wal

from datetime import datetime
name = raw_input("What is your name:")
adress = raw_input("What is you Address")
dt_bday = raw_input("Your Birthday (dd/mm/yyy):")
year_from_my_bday = dt_bday.split("/")[2]
actual_year = datetime.now().year
my_personal_year = actual_year - int(year_from_my_bday)
print("{},{},{},{},{}".format(name, adress, dt_bday, actual_year, my_personal_year))
#Jus a new comment!!!
#Just Another
