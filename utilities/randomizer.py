from faker import Faker
import random
from utilities.data_time_utils import get_timestamp


class Randomize:
    def __init__(self):
        self.faker: Faker = Faker(locale='en_us')

    def random_first_name(self):
        return self.faker.first_name()

    def random_username(self):
        return f'{self.faker.first_name()}_{get_timestamp()}'

    def random_last_name(self):
        return self.faker.last_name()

    def random_email_id(self, first_name=None, last_name=None):
        if first_name is None:
            first_name = self.random_first_name()
        if last_name is None:
            last_name = self.random_last_name()
        name = (first_name + '.' + last_name).lower()
        domain = self.faker.domain_name()
        email = f'{name}@{domain}'
        return email

    def random_phone_number_without_country_code(self):
        phone = ('+91' + "%02d" % self.faker.random.randint(70, 99)) + \
                ("%08d" % self.faker.random.randint(0, 99999999))
        return phone

    def random_long_integer(self, lower_limit=0, upper_limit=999999999):
        return self.faker.random.randint(lower_limit, upper_limit)

    def random_integer(self, lower_limit=0, upper_limit=65535):
        return self.faker.random.randint(lower_limit, upper_limit)

    def random_short_integer(self, lower_limit=0, upper_limit=255):
        return self.faker.random.randint(lower_limit, upper_limit)

    def random_integer_from_length(self, length=1):
        return self.faker.random.randint(0, int('9' * length))

    def random_password(self, length=10):
        return self.faker.password(length)

    def random_urls(self, number=10):
        number_of_urls = self.random_integer(0, number)
        lst = []
        base = self.faker.url()
        for _ in range(number_of_urls):
            file_name = self.faker.file_name(extension=random.choice(['jpg', 'png', 'bmp']))
            lst.append(f'{base}{file_name}')
        return lst

    def random_words(self, number=3):
        return ' '.join(self.faker.words(number, unique=True))
