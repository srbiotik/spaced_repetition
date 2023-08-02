from datetime import datetime

def print_header():
    """ Prints resource """
    print(f'#  {"name".ljust(75)} {"url".ljust(75)} due_time')
    print(f'___{"".ljust(79, "_")}{"".ljust(78, "_")}_________')

def print_resource(resource):
    """ Prints resource """
    print(f'{str(resource.doc_id)}. {resource["name"].ljust(75)} {resource["url"].ljust(75)} {resource["due_time"]}')


def string_to_date(string):
    """ Converts a string representation of datetime to obj """
    return datetime.strptime(string, "%Y-%m-%d")

def date_to_string(date):
    """ Convert to string, in the format of year-month-day """
    return date.strftime("%Y-%m-%d")
