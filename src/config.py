import os
import json
import yaml


with open('config.yaml', 'r') as yaml_file:
    config = yaml.load(yaml_file, yaml.Loader)

if not os.path.isfile(config['logs_path']):
    with open(config['logs_path'], mode='w', encoding='utf-8') as log:
        json.dump([], log)
