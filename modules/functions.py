import sys, os

class Functions:
    def __init__(self) -> None:
        pass
    
    def get_asset_dir(self):
        if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
            imageDir = os.path.join(sys._MEIPASS)
        else:
            imageDir = os.getcwd()
        return imageDir
    
    def get_asset(self, assetName):
        return self.get_asset_dir()+ "/assets/" + assetName
    
    def visibler(self, element, status):
        element.visible = status
        element.update()
        
    def text_set(self, element, updateElement, text):
        element.value = text
        updateElement.update()