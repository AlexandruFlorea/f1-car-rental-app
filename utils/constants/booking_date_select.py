import json

# AVAILABLE_HOURS = [('11', '11:00'),
#                    ('12', '12:00'),
#                    ('13', '13:00'),
#                    ('14', '14:00'),
#                    ('15', '15:00')]

with open(r'G:\Python\f1-car-rental-app\tracks\fixtures\tracks-availability.json') as jsonfile:
    jsonobj = json.load(jsonfile)

time_dict = jsonobj['fields']

AVAILABLE_HOURS = [(key, value) for key, value in time_dict['time'].items()]
AVAILABLE_YEARS = [(key, value) for key, value in time_dict['year'].items()]
AVAILABLE_MONTHS = [(key, value) for key, value in time_dict['month'].items()]
AVAILABLE_DAYS = [(key, value) for key, value in time_dict['day'].items()]

# print(jsonobj)
# print(AVAILABLE_YEARS)
