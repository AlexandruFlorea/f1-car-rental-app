import json
import re


def parse_facts(soup):
    facts = []
    for p_tag in soup.findAll('p'):
        if re.match("^[0-9]", p_tag.text):  # check if the paragraph starts with digits
            facts.append(p_tag.text)

    return facts


def write_output(facts):
    with open('output/data.json', 'w+') as json_file:
        json.dump(facts, json_file, indent=2)


def parse_facts2(soup):
    facts = []
    for p_tag in soup.findAll('p'):
        if re.match("^[0-9]", p_tag.text):  # check if the paragraph starts with digits
            facts.append(p_tag.text)

    return facts


# def write_output2(facts):
#     with open('output/data.json', 'a') as json_file:
#         json.dump(facts, json_file, indent=2)
