

from datetime import date

date_1 = date(2014, 7, 2)
date_2 = date(2014, 7, 11)
delta = date_2 - date_1
print(delta.days)