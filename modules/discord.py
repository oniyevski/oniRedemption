import psutil, threading, time
from pypresence import Presence
from modules.functions import Functions

class Discord(threading.Thread):
    def __init__(self, content, config):
        threading.Thread.__init__(self)
        self.content = content
        self.config = config
        self.clientID = "1177622601808490576"
        self.rpc = Presence(self.clientID, pipe=0)
        self.buttons = [
            {
                "label": self.config.get_local_text('rpc_download_software'), 
                "url": "https://github.com/oniyevski/oniRedemption/releases"
            }, 
            {
                "label": self.config.get_local_text('rpc_author_page'), 
                "url": "https://oniyevski.pw/"
            }
        ]
        self.epochTime = 0
        self.epochFix = False
        
    def rpc_connect(self):
        try:
            self.rpc.connect()
            return True
        except:
            return False
        
    def start_rpc(self):
        while True:
            if self.config.lastConfig["settings"]["discord_integration"]:  
                try:
                    if self.content.page == "start":
                        self.epochFix = False
                        self.rpc.update(
                            details=self.config.get_local_text('rpc_homepage'),
                            large_image="logo",
                            buttons=self.buttons
                        )
                    elif self.content.page == "shield":
                        self.epochFix = False
                        if self.config.lastConfig["settings"]["shield_status"] and self.config.lastConfig["settings"]["shield_password"] is not None:
                            self.rpc.update(
                                details=f"{self.config.get_local_text('rpc_shield_password')} " + (self.config.lastConfig["settings"]["shield_password"] if self.config.lastConfig["settings"]["discord_shield_password_view"] and self.config.lastConfig["settings"]["shield_password"] is None else str(self.config.lastConfig["settings"]["shield_password"])[:2]+"********"),
                                state=f"{self.config.get_local_text('rpc_shield_status')} " + (self.config.get_local_text('rpc_active') if self.config.lastConfig["settings"]["shield_status"] else self.config.get_local_text('rpc_deactive')),
                                large_image="logo",
                                buttons=self.buttons
                            )
                        else:
                            self.rpc.update(
                                details=f"{self.config.get_local_text('rpc_shield_status')} " + self.config.get_local_text('rpc_deactive'),
                                large_image="logo",
                                buttons=self.buttons
                            )
                    elif self.content.page == "settings":
                        self.epochFix = False
                        self.rpc.update(
                            details=self.config.get_local_text('rpc_settings'),
                            large_image="logo",
                            buttons=self.buttons,
                        )
                    elif self.content.page == "chronometer":
                        if self.content.whileBreak:
                            self.epochFix = False
                            self.rpc.update(
                                details=self.config.get_local_text('rpc_mission_completed'),
                                state=self.config.get_local_text(f'{self.content.minute}_minute'),
                                large_image="logo",
                                buttons=self.buttons
                            )
                        else:
                            if self.epochFix == False:
                                self.epochTime = int(time.time())
                                self.epochFix = True
                            self.rpc.update(
                                details=self.config.get_local_text('rpc_on_mission'),
                                state=self.config.get_local_text(f'{self.content.minute}_minute'),
                                large_image="logo",
                                buttons=self.buttons,
                                start=self.epochTime
                            )
                except:
                    pass
                time.sleep(5)
            else:
                time.sleep(2)