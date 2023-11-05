import json

#cars_json='{"mark":"honda","model":"HVR"}'

#cars = json.loads(cars_json)

"""for k, e in cars.items():
    print(f'{k}: {e}')"""

cars = {"mark":"honda","model":"HVR"}

cars_json=json.dumps(cars)

