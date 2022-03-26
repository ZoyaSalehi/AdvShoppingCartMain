
from faker import Faker
fake = Faker(locale=['en_CA', 'en_US'])

app = "Advantage Online Shopping"
aos_URL = "https://advantageonlineshopping.com/#/"
#aos_homepage_title = f"\u00A0Advantage Shopping"
#aos_homepage_title = "&nbspAdvantage Shopping".replace('&nbsp', '')
aos_homepage_title = " Advantage Shopping"
aos_register_URL = "https://advantageonlineshopping.com/#/register"
new_username = fake.user_name()
new_password = fake.password()
email = fake.email()
first_name = fake.first_name()
last_name = fake.last_name()
phonenum = fake.phone_number()
full_name = f'{first_name} {last_name}'
address = fake.street_address()

while len(fake.city())>9 or len(fake.city())==0 :
    city = fake.city()

short_city = city

country = fake.current_country()
state = fake.state()
zip_code = fake.zipcode()