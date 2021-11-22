# from django.core.exceptions import ValidationError
# from utils.constants.booking_date_select import BOOKED_YEARS, BOOKED_MONTHS, BOOKED_DAYS, BOOKED_HOURS
#
#
# def validate_year(year):
#     if year in BOOKED_YEARS:
#         raise ValidationError('No slot available for the selected year.')
#
#     return year
#
#
# def validate_month(month):
#     if month in BOOKED_MONTHS:
#         raise ValidationError('No slot available for the selected month.')
#
#     return month
#
#
# def validate_day(day):
#     if day in BOOKED_DAYS:
#         raise ValidationError('No slot available for the selected day.')
#
#     return day
#
#
# def validate_time(time):
#     if time in BOOKED_HOURS:
#         raise ValidationError('Selected slot not available.')
#
#     return time
