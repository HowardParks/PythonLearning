import requests
import datetime
import os
from dotenv import load_dotenv
project_folder=os.path.expanduser('~/health_tracker')
load_dotenv(os.path.join(project_folder, '.env'))

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
# gottobtru@gmail.com, HowardP, Whi5tle Tasty Delight
GENDER = 'male'
WEIGHT_KG = 104
HEIGHT_CM = 168
AGE = 62
BASIC = os.getenv("BASIC")

nutritionix_ep = 'https://trackapi.nutritionix.com/v2'
natlang_exercise_ep = f"{nutritionix_ep}/natural/exercise"
headers = {
    'Content-Type': 'application/json',
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}
now = datetime.datetime.now()
ddate = now.strftime("%m/%d/%Y")
dtime = now.strftime("%X")
query = input("How did you exercise today? ")
params = {
    'query': query,
    'gender': GENDER,
    'weight_kg': WEIGHT_KG,
    'height_cm': HEIGHT_CM,
    'age': AGE
}
# print(query)
response = requests.post(url=natlang_exercise_ep, headers=headers, json=params)
response.raise_for_status()
results = response.json()

sheety_endpoint = os.getenv("SHEETY_ENDPOINT")
sheety_headers = {
    'Content-Type': 'application/json',
    'Authorization': BASIC
    }
for e in results['exercises']:
    sheety_params = {
        'workout': {
            'date': ddate,
            'time': dtime,
            'exercise': e['name'],
            'duration': e['duration_min'],
            'calories': e['nf_calories']
        }
    }
    response = requests.post(url=sheety_endpoint, headers=sheety_headers, json=sheety_params)
    response.raise_for_status()
    results = response.json()
#    print(results)
    print(f"{e['duration_min']} minutes of {e['name']} uses {e['nf_calories']} calories.")
