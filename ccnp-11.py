import csv
import json

with open('device.csv','r') as devices:
    device_dict = csv.DictReader(devices)
    for device in device_dict:
        print(json.dumps(device,indent=4))