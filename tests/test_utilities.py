from bot.utilities import count_characters
from faker import Faker

def test_count_characters():
    count = 27
    faker = Faker()
    text = faker.texts(nb_texts = count)
    assert count_characters(text) == count