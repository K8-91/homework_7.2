from faker import Faker
fake = Faker()


class BaseContact:
    def __init__(self, name, private_number, email):
       self.name = name
       self.private_number = private_number
       self.email = email
    def __str__(self):
        return f'{self.name} {self.private_number} {self.email}'
    def __repr__(self):
        return f'{self.name} {self.private_number} {self.email}'
    def contact(self):
        return f"Wybieram numer {self.private_number} i dzwonię do {self.name}"

    

class BusinessContact(BaseContact):
    def __init__(self, position, company_name, work_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = position
        self.company_name = company_name
        self.work_number = work_number
    def __str__(self):
        return f'{self.name} {self.private_number} {self.email} {self.position}, {self.company_name}, {self.work_number}'
    def __repr__(self):
        return f'{self.name} {self.private_number} {self.email} {self.position}, {self.company_name}, {self.work_number}'

    def contact(self):
        return f"Wybieram numer {self.work_number} i dzwonię do {self.name}"  


def create_contacts(contact_type, quantity):
    if contact_type == 'base':
        for base_contact in range(quantity):
            base_contact = BaseContact(name=fake.name(), private_number=fake.phone_number(), email=fake.email() )
            print(base_contact)
            print(base_contact.contact())
    if contact_type == 'business':
        for business_contact in range(quantity):
            business_contact=BusinessContact(name=fake.name(), private_number=fake.phone_number(), email=fake.email(), position=fake.job(), company_name=fake.company(), work_number=fake.phone_number() )
            print(business_contact)
            print(business_contact.contact())

  




