from sqlalchemy.orm import Session
from sqlalchemy import create_engine

class Customer:
    def __init__(self,first_name,last_name,username,email, address,town):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = username
        self.email = email
        self.address = address
        self.town = town

    def __repr__(self):
        return "{} {} {} {} {} {}".format(self.first_name, self.last_name, self.user_name, self.email, self.address, self.town)

engine = create_engine("postgres+psycopg2://postgres:pass@localhost/mydb")
session = Session(bind=engine)

from sqlalchemy.orm import sessionmaker, Session
Session = sessionmaker(bind=engine)

session = Session()

c1 = Customer(first_name='Toby',
              last_name='Miller',
              username='tmiller',
              email='tmiller@example.com',
              address='1662 Kinney Street',
              town='Wolfden'
              )

c2 = Customer(first_name='Scott',
              last_name='Harvey',
              username='scottharvey',
              email='scottharvey@example.com',
              address='424 Patterson Street',
              town='Beckinsdale'
              )
print("Customer 1 is: {}".format(c1))
print("Customer 2 is: {}".format(c2))