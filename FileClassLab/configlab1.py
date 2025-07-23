import configparser

path='C://Users/Owner/PycharmProjects/PythonLearning/FileClassLab/'
config = configparser.ConfigParser()
config.read(path+'mess.ini')
prodcon = configparser.ConfigParser()
devcon = configparser.ConfigParser()

sections = config.sections()
for sec in sections:
    keys  = list(config[sec].keys())
    if 'env' in keys:
        if config[sec]['env'] == 'dev':
            devcon.add_section(sec)
            for key in config[sec].keys():
                if key == 'env':
                    continue
                devcon[sec][key] = config[sec][key]
        if config[sec]['env'] == 'prod':
            prodcon.add_section(sec)
            for key in config[sec].keys():
                if key == 'env':
                    continue
                prodcon[sec][key] = config[sec][key]
with open('prod_config.ini', 'w') as configfile:
    prodcon.write(configfile)
with open('dev_config.ini', 'w') as configfile:
    devcon.write(configfile)