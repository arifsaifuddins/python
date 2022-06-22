# modules

# core modules
import datetime
from datetime import date
from time import time

# pip modules
import camelcase

# import file module
import validator
from validator import validate_email

today = datetime.date.today()

today1 = date.today()

c = camelcase.CamelCase()

email = 'test@mail.com'

print(validate_email(email))

print(c.hump('hello arief saif'))
print(today)
print(today1)
print(time())
