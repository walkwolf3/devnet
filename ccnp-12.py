import yaml
import json

with open('device01.yml','r') as f:
    yml_file = f.read()
    detail1 = yaml.full_load(yml_file)
    json1 = json.dumps(detail1,indent=4)

    data2 = yaml.dump(json1,indent=4)
    print(data2)

