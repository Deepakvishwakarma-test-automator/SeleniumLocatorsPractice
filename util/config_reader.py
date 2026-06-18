import configparser

class ConfigReader:
    def __init__(self, file_path="config/config.ini"):
        self.config = configparser.ConfigParser()
        self.config.read(file_path)

    def get(self, section, key):
        return self.config[section][key]
