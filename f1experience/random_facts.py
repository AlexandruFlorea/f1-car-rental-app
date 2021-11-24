from random import choice


with open(r'G:\Python\f1-car-rental-app\web_scraping\output\data.json', encoding='utf-8') as f:
    facts = [
        fact.rstrip('\r\n ').replace('"', '')
        for fact in f.readlines()
        if fact.rstrip('\r\n ') != '' or len(fact) < 5
    ]


def get_fact() -> str:
    random_fact = choice(facts)

    return random_fact
