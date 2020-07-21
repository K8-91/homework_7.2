from faker import Faker
fake = Faker()


class BaseContact:
    def __init__(self, first_name, last_name, private_number, email):
       self.first_name = first_name
       self.last_name = last_name
       self.private_number = private_number
       self.email = email
       self._label_lenght=[]
    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.private_number} {self.email}'
    def __repr__(self):
        return f'{self.first_name} {self.last_name} {self.private_number} {self.email}'
    def contact(self):
        return f"Wybieram numer {self.private_number} i dzwonię do {self.first_name} {self.last_name}"
    @property
    def label_length(self):
        return self._label_lenght

    @label_length.setter
    def label_lenght(self, name):
        self.first_name = name[0]
        self.last_name = name[1]
        self._label_lenght= print(len(name[0]), len(name[1]))
    

    
class BusinessContact(BaseContact):
    def __init__(self, position, company_name, work_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = position
        self.company_name = company_name
        self.work_number = work_number
    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.private_number} {self.email} {self.position}, {self.company_name}, {self.work_number}'
    def __repr__(self):
        return f'{self.first_name} {self.last_name} {self.private_number} {self.email} {self.position}, {self.company_name}, {self.work_number}'

    def contact(self):
        return f"Wybieram numer {self.work_number} i dzwonię do {self.first_name} {self.last_name}"  

contact_list=[]
def create_contacts(contact_type, quantity):
    if contact_type == 'base':
        for base_contact in range(quantity):
            base_contact = BaseContact(first_name=fake.first_name(), last_name=fake.last_name(),  private_number=fake.phone_number(), email=fake.email() )
            contact_list.append(base_contact)
            base_contact.label_lenght = [base_contact.first_name, base_contact.last_name]
    if contact_type == 'business':
        for business_contact in range(quantity):
            business_contact=BusinessContact(first_name=fake.first_name(), last_name=fake.last_name(), private_number=fake.phone_number(), email=fake.email(), position=fake.job(), company_name=fake.company(), work_number=fake.phone_number() )
            contact_list.append(business_contact)
            business_contact.label_lenght = [business_contact.first_name, business_contact.last_name]
    return contact_list

print(create_contacts('business', 4))





