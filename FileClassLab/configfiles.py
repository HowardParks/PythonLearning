import configparser

config = configparser.ConfigParser()

dict = {
    'DEFAULT': {
        'host': 'localhost'
    },
    'mariadb': {
        'name': 'hello',
        'user': 'root',
        'password': 'password'
    },
    'redis': {
        'port': 6379,
        'db': 0
    }
}

config.read_dict(dict)
sections = config.sections()
print('Sections:', config.sections(),'\n')


print('mariadb section:')

print('Host:', config['mariadb']['host'])
print('Database:', config['mariadb']['name'])
print('Username:', config['mariadb']['user'])
print('Password:', config['mariadb']['password'], '\n')

print('redis section:')
print('Host:', config['redis']['host'])
print('Port:', int(config['redis']['port']))
print('Database number:', int(config['redis']['db']))

###### Or #####
config = configparser.ConfigParser()
print(config.read('configinterp.ini'))

sections = config.sections()
for sec in sections:
    print(f"{sec} section:")
    mkeys = list(config[sec].keys())
    for k in mkeys:
        print(k.capitalize()+':',config[sec][k])

##### And #####
config = configparser.ConfigParser()

config['DEFAULT'] = {'host': 'localhost'}
config['mariadb'] = {'name': 'hello',
                     'user': 'root',
                     'password': 'password'}
config['redis'] = {'port': 6379,
                   'db': 0,
                   'server': '%(host)s'}


with (open('config.ini', 'w') as configfile):
    config.write(configfile)
