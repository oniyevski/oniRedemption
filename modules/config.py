import json


class Config:
    def __init__(self):
        self.lastConfig = {}
    
    def config_loader(self):
        try:
            f = open(f'config.json', encoding="utf-8") 
            self.lastConfig = json.load(f)
            f = open(f'languages.json', encoding="utf-8") 
            self.lastConfig["languages"] = json.load(f)["languages"]
            return True
        except:
            return False
        
    def write_config(self):
        with open('config.json', 'w', encoding='utf-8') as f:
            json.dump({"settings": self.lastConfig["settings"]}, f, ensure_ascii=False, indent=4)
        self.config_loader()

    def get_local_text(self, key):
        return self.lastConfig["languages"][self.lastConfig["settings"]["language"]][key]
