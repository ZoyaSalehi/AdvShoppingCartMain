
from faker import Faker
fake = Faker(locale=['en_CA', 'en_US'])

app = "Advantage Online Shopping"
aos_URL = "https://advantageonlineshopping.com/#/"
aos_homepage_title = f"\u00A0Advantage Shopping"
#aos_homepage_title = "&nbspAdvantage Shopping".replace('&nbsp', '')
#aos_homepage_title = " Advantage Shopping"
aos_register_URL = "https://advantageonlineshopping.com/#/register"
new_username = fake.user_name()
new_password = fake.password()
email = fake.email()

init_first_name = fake.first_name()
if len(init_first_name)>15:
    first_name = init_first_name[:15:]
else:
    first_name = init_first_name

last_name = fake.last_name()

init_phonenum = fake.phone_number()
if len(init_phonenum)>10:
    phonenum = init_phonenum[:10:]
else:
    phonenum = init_phonenum

full_name = f'{first_name} {last_name}'
address = fake.street_address()

init_city = fake.city()
if len(init_city)>10:
    city = init_city[:10:]
else:
    city = init_city

country = fake.current_country()

init_state = fake.state()
if len(init_state)>10:
    state = init_state[:10:]
else:
    state = init_state

zip_code = fake.zipcode()
counter = 0

description = fake.sentence(nb_words=10)