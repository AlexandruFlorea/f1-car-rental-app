from random import choice
import os
from f1experience.settings.base import BASE_DIR


with open(os.path.join(BASE_DIR, 'web_scraping/output/data.json')) as f:
    facts = [
        fact.rstrip('\r\n ').replace('"', '')
        for fact in f.readlines()
        if fact.rstrip('\r\n ') != '' or len(fact) < 5
    ]


def get_fact() -> str:
    random_fact = choice(facts)

    return random_fact
