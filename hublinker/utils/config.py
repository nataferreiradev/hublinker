import configparser
import keyring

class ConfigManager:
    def __init__(self, config_file='config.ini', section='DEFAULT'):
        self.config_file = config_file
        self.section = section
        self.config = configparser.ConfigParser()
        self.config.read(self.config_file)

        if self.section not in self.config:
            self.config[self.section] = {}
            self._save_config()

    def _save_config(self):
        with open(self.config_file, 'w') as config_file:
            self.config.write(config_file)

    def set(self, key, value):
        if self.section not in self.config:
            self.config[self.section] = {}
        self.config[self.section][key] = str(value)
        self._save_config()

    def get(self, key, default=None):
        return self.config[self.section].get(key, default)

    def get_int(self, key, default=None) -> int | None:
        value = self.get(key,default)
        if not value:
            return None
        return int(self.get(key,default))
    
    def set_token(token):
       keyring.set_password("hublinker", "token", token)

    def get_token():
        return keyring.get_password("hublinker", "token")