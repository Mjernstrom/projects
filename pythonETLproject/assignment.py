import sqlalchemy as db
import json
from datetime import datetime
from dateutil.relativedelta import relativedelta

class Customer:

    def __init__(self, id, fname, lname, dob, city, state, zip):
        self.id = id
        self.first_name = fname
        self.last_name = lname
        self.dob = dob
        self.city = city
        self.state = state
        self.zip = zip
        self.student_name = 'Matthew Jernstrom'

    def full_name(self):
        full_name = self.first_name + ' ' + self.last_name
        return full_name

    def age(self):
        dob_new = datetime.strptime(self.dob, '%Y-%m-%d')
        today = datetime.today()
        age = relativedelta(today, dob_new)
        return age.years

    def adult(self):
        return self.age >= 18

    def to_json(self):
        self.full_name = self.full_name()
        self.age = self.age()
        self.adult = self.adult()
        dict = {
            'id': self.id,
            'first_name': self.first_name,
            "last_name": self.last_name,
            "dob": self.dob,
            "city": self.city,
            "state": self.state,
            "zip": self.zip,
            "age": self.age,
            "full_name": self.full_name,
            "adult": self.adult
        }
        return dict


def main():
	# connect and read from customer.sqlite
    engine = db.create_engine('sqlite:///customer.sqlite')
    connection = engine.connect()

    # get all the attributes from the customer table
    results = connection.execute("select * from customer")

    # create a list of customer objects
    customers = []
    for row in results:
        c = Customer(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        customers.append(c.to_json())

    # close the database connection
    connection.close()

    # output to a json file
    with open('customers_assignment6.json', 'w') as output:
        json.dump(customers, output, sort_keys=True, indent=4)


main()
