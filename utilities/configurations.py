import configparser


def getConfig():
    config = configparser.ConfigParser()
    config.read('utilities/properties.ini')
    return config

def getPassword():
    return 'A1u2s3t4i5n6tri'
