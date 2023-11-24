import os, threading
from time import sleep
from flet import *
from ui.colors import *
from ui.header import Header
from ui.footer import Footer
from ui.content import Content
from modules.functions import Functions
from modules.config import Config
from modules.process import Process
from modules.modal import Modal
from modules.discord import Discord

config = Config()

headerClass = Header(config)
footerClass = Footer(config)
contentClass = Content(config)
func = Functions()

discord = Discord(content=contentClass, config=config)

class UI(UserControl):
    def MainContainer(self):
        self.main_container = Column(
            spacing=30,
            controls=[
                headerClass.header,
                contentClass.content,
                footerClass.footer
            ]
        )
        return self.main_container

    def build(self):
        return Column(controls=[self.MainContainer()])

def start(page: Page):
    page.dark_theme = theme.Theme(color_scheme_seed=FG)
    page.theme_mode = ThemeMode.DARK
    page.window_frameless = True
    page.window_width = 750
    page.window_height = 680
    page.title = "ONIREDEMPTION"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.bgcolor = BG
    page.padding = 20
    page.window_center()
    app = UI()
    page.overlay.append(
        Audio(
            src=func.get_asset("success.mp3")
        )
    )
    page.overlay.append(
        Audio(
            src=func.get_asset("shield.mp3")
        )
    )
    page.overlay.append(
        Audio(
            src=func.get_asset("move.mp3")
        )
    )
    page.add(app)
    sleep(2)
    configLoad = config.config_loader()
    if configLoad:
        if config.lastConfig["settings"]["rdr_path"] == "" or os.path.exists(config.lastConfig["settings"]["rdr_path"]) == False or os.path.exists(config.lastConfig["settings"]["rdr_path"] + "\\RDR2.exe") == False:
            func.text_set(contentClass.control_label, contentClass.control_label_container, config.get_local_text('rdr2_file_location_unfound'))
            sleep(3)
            func.text_set(contentClass.control_label, contentClass.control_label_container, config.get_local_text('wizard_starting'))
            sleep(3)
            func.text_set(contentClass.control_label, contentClass.control_label_container, config.get_local_text('start_rdr2_game'))
            sleep(5)
            rdr2 = Process("RDR2.exe")
            while True:
                func.text_set(contentClass.control_label, contentClass.control_label_container, config.get_local_text('rdr2_waiting'))
                sleep(2)
                rdr2Status = rdr2.getProcessStatus()
                if rdr2Status != "error" and rdr2Status != "stopped":
                    break
                elif rdr2Status == "error":
                    func.text_set(contentClass.control_label, contentClass.control_label_container, config.get_local_text('an_error_occurred_while_waiting_for_rdr2'))
                    sleep(3)
                    page.window_close()
                    break
            config.lastConfig["settings"]["rdr_path"] = os.path.join(rdr2Status)
            config.write_config()
            modal = Modal(
                app, 
                config.get_local_text('great_modal_title'), config.get_local_text('wizard_success'),
            )
            modal.set_actions([
                    TextButton(config.get_local_text('modal_understood'), on_click=modal.close_dlg, style=ButtonStyle(color=REDEMPTION)),
                ]
            )
            modal.open_dlg()
        func.visibler(contentClass.control, False)
        func.visibler(contentClass.select_minute, True)
        func.visibler(contentClass.rail, True)
        contentClass.general_container.height = 400
        contentClass.general_container.update()
        if discord.rpc_connect():
            t1 = threading.Thread(
                target=discord.start_rpc
            )
            t1.start()
    else:
        func.text_set(contentClass.control_label, contentClass.control_label_container, config.get_local_text('config_json_error'))
        sleep(3)
        page.window_close()
    