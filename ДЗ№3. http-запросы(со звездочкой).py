import requests
from pprint import pprint

url = 'https://stackoverflow.com/2.3/questions'
params = {
    'fromdate': '1674864000', 
    'todate': '1674950400', 
    'order': 'desc', 
    'sort': 'activity', 
    'tagged': 'Python', 
    'site': 'stackoverflow'
}
response = requests.get(url, params)
pprint(response.json())