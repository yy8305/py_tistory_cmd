import json, os

print('config init')
home_dir = os.path.expanduser('~')
base_dir = home_dir + '\\.tistory_cmd'
config_file = base_dir + '\\config.json'
config_json = dict()
config_json['app_id'] = ''
config_json['secret_key'] = ''
config_json['access_code'] = ''
config_json['access_token'] = ''

config = ''

if not os.path.exists(base_dir):
    os.makedirs(base_dir)

if not os.path.exists(config_file):
    with open(config_file, 'w', encoding='utf-8') as make_file:
        json.dump(config_json, make_file, indent="\t")

with open(config_file, 'r') as f:
    config = json.load(f)


def set_config():
    with open(config_file, 'w', encoding='utf-8') as make_file:
        json.dump(config, make_file, indent="\t")


def reset_access_token():
    config['access_code'] = ''
    config['access_token'] = ''
    set_config()