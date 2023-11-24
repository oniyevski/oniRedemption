import os
from time import sleep
from flet import *
from ui.colors import *
from modules.chronometer import Chronometer
from modules.modal import Modal
from modules.functions import Functions
from modules.process import Process

class Content:
    def __init__(self, config):
        self.extraPages = ["shield", "settings"]
        
        self.config = config
        
        self.config.config_loader()
        
        self.loadedLanguage = self.config.lastConfig["settings"]["language"]
        
        self.whileBreak = True
        
        self.page = "start"
        
        def select_minute_dropdown_change(e):
            self.minute = self.select_minute_dropdown.value
            
        def language_dropdown_change(e):
            self.config.lastConfig["settings"]["language"] = e.control.value
            self.config.write_config()
            if e.control.value == self.loadedLanguage:
                self.program_restart.visible = False
            else:
                self.program_restart.visible = True
            self.settings.update()
        
        def settings_change(e, key):
            if e.control.value == True:
                e.control.thumb_color = REDEMPTION
            else:
                e.control.thumb_color = WHITE
            self.settings.update()
            self.config.lastConfig["settings"][key] = e.control.value
            self.config.write_config()
            if self.config.lastConfig["settings"]["sound_effects"]:
                e.page.overlay[2].play()
                
        def shield_click(e):
            func = Functions()
            if self.page == "chronometer":
                modal = Modal(
                    e, 
                    self.config.get_local_text("hey_modal_title"), self.config.get_local_text("the_stopwatch_is_working"),
                )
                modal.set_actions([
                        TextButton(self.config.get_local_text("modal_understood"), on_click=modal.close_dlg, style=ButtonStyle(color=REDEMPTION)),
                    ]
                )
                modal.open_dlg()
                return
            self.page = "shield"
            self.shield_container.content.bgcolor = REDEMPTION
            self.settings_container.content.bgcolor = BG
            self.timer_container.content.bgcolor = BG
            self.rail.update()
            func.visibler(self.select_minute, False)
            func.visibler(self.settings, False)
            func.visibler(self.shield, True)
            
        def shield_change(e):
            rdr2 = Process("RDR2.exe")
            rdr2Status = rdr2.getProcessStatus()
            if rdr2Status != "error" and rdr2Status != "stopped":
                modal = Modal(
                    e, 
                    self.config.get_local_text("hey_modal_title"), self.config.get_local_text("rdr2_running_modal"),
                )
                modal.set_actions([
                        TextButton(self.config.get_local_text("modal_understood"), on_click=modal.close_dlg, style=ButtonStyle(color=REDEMPTION)),
                    ]
                )
                modal.open_dlg()
                if e.control.value == True:
                    e.control.value = False
                else:
                    e.control.value = True
                self.shield.update()
                return
            if self.shield_password.value == "":
                modal = Modal(
                    e, 
                    self.config.get_local_text("hey_modal_title"), self.config.get_local_text("password_part_blank_not_leavable"),
                )
                modal.set_actions([
                        TextButton(self.config.get_local_text("modal_understood"), on_click=modal.close_dlg, style=ButtonStyle(color=REDEMPTION)),
                    ]
                )
                modal.open_dlg()
                if e.control.value == True:
                    e.control.value = False
                else:
                    e.control.value = True
                self.shield.update()
                return
            if e.control.value == True:
                try:
                    self.shield_password.disabled = True
                    xml = '<?xml version="1.0" encoding="UTF-8"?><CDataFileMgr__ContentsOfDataFileXml><disabledFiles /><includedXmlFiles itemType="CDataFileMgr__DataFileArray" /><includedDataFiles /><dataFiles itemType="CDataFileMgr__DataFile"><Item><filename>platform:/data/cdimages/scaleform_platform_pc.rpf</filename><fileType>RPF_FILE</fileType></Item><Item><filename>platform:/data/ui/value_conversion.rpf</filename><fileType>RPF_FILE</fileType></Item><Item><filename>platform:/data/ui/widgets.rpf</filename><fileType>RPF_FILE</fileType></Item><Item><filename>platform:/textures/ui/ui_photo_stickers.rpf</filename><fileType>RPF_FILE</fileType></Item><Item><filename>platform:/textures/ui/ui_platform.rpf</filename><fileType>RPF_FILE</fileType></Item><Item><filename>platform:/data/ui/stylesCatalog</filename><fileType>aWeaponizeDisputants</fileType></Item><Item><filename>platform:/data/cdimages/scaleform_frontend.rpf</filename><fileType>RPF_FILE_PRE_INSTALL</fileType></Item><Item><filename>platform:/textures/ui/ui_startup_textures.rpf</filename><fileType>RPF_FILE</fileType></Item><Item><filename>platform:/data/ui/startup_data.rpf</filename><fileType>RPF_FILE</fileType></Item></dataFiles><contentChangeSets itemType="CDataFileMgr__ContentChangeSet" /><patchFiles /></CDataFileMgr__ContentsOfDataFileXml>'+self.shield_password.value
                    f = open(self.config.lastConfig["settings"]["rdr_path"] + "\\x64\\data\\startup.meta", "w")
                    f.write(xml)
                    f.close()
                except:
                    if e.control.value == True:
                        e.control.value = False
                    else:
                        e.control.value = True
                    self.shield.update()
                    modal = Modal(
                        e, 
                        self.config.get_local_text("hey_modal_title"), self.config.get_local_text("rdr2_running_this_process_failed"),
                    )
                    modal.set_actions([
                            TextButton(self.config.get_local_text("modal_understood"), on_click=modal.close_dlg, style=ButtonStyle(color=REDEMPTION)),
                        ]
                    )
                    modal.open_dlg()
                    return
            else:
                if os.path.exists(config.lastConfig["settings"]["rdr_path"] + "\\x64\\data\\startup.meta"):
                    try:
                        os.remove(config.lastConfig["settings"]["rdr_path"] + "\\x64\\data\\startup.meta")
                        self.shield_password.disabled = False
                    except:
                        if e.control.value == True:
                            e.control.value = False
                        else:
                            e.control.value = True
                        self.shield.update()
                        modal = Modal(
                            e, 
                            self.config.get_local_text("hey_modal_title"), self.config.get_local_text("rdr2_running_this_process_failed"),
                        )
                        modal.set_actions([
                                TextButton(self.config.get_local_text("modal_understood"), on_click=modal.close_dlg, style=ButtonStyle(color=REDEMPTION)),
                            ]
                        )
                        modal.open_dlg()
                        return
            if e.control.value == True:
                e.control.thumb_color = REDEMPTION
                if self.config.lastConfig["settings"]["sound_effects"]:
                    e.page.overlay[1].play()
            else:
                e.control.thumb_color = WHITE
                if self.config.lastConfig["settings"]["sound_effects"]:
                    e.page.overlay[2].play()
            self.shield.update()
            self.config.lastConfig["settings"]["shield_password"] = self.shield_password.value
            self.config.lastConfig["settings"]["shield_status"] = e.control.value
            self.config.write_config()
        
        def settings_click(e):
            func = Functions()
            if self.page == "chronometer":
                modal = Modal(
                    e, 
                    self.config.get_local_text("hey_modal_title"), self.config.get_local_text("the_stopwatch_is_working"),
                )
                modal.set_actions([
                        TextButton(self.config.get_local_text("modal_understood"), on_click=modal.close_dlg, style=ButtonStyle(color=REDEMPTION)),
                    ]
                )
                modal.open_dlg()
                return
            self.page = "settings"
            self.shield_container.content.bgcolor = BG
            self.settings_container.content.bgcolor = REDEMPTION
            self.timer_container.content.bgcolor = BG
            self.rail.update()
            func.visibler(self.select_minute, False)
            func.visibler(self.shield, False)
            func.visibler(self.settings, True)
            
        def stop_click(e="bypass"):
            func = Functions()
            if e != "bypass":
                self.page = "start"
                self.shield_container.content.content.color = WHITE
                self.shield_container.update()
                self.settings_container.content.content.color = WHITE
                self.settings_container.update()
            func.visibler(self.timer_container, True)
            func.visibler(self.timer_stop_container, False)
            func.visibler(self.select_minute, True)
            func.visibler(self.minute_part, False)
            self.gold_bar.image_src = func.get_asset("0.00.png")
            self.gold_bar.update()
            self.progressbar.value = None
            self.progressbar_container.update()
            self.percent.value = "%0.00"
            self.percent_container.update()
            self.remaining_time.value = f"0 {self.config.get_local_text('minute')}, 0 {self.config.get_local_text('second')}"
            self.remaining_time_container.update()
            self.whileBreak = True
            
        def start_click(e):
            func = Functions()
            if self.page in self.extraPages:
                func.visibler(self.settings, False)
                func.visibler(self.shield, False)
                func.visibler(self.select_minute, True)
                self.page = "start"
                self.shield_container.content.bgcolor = BG
                self.settings_container.content.bgcolor = BG
                self.timer_container.content.bgcolor = REDEMPTION
                self.rail.update()
                return
            if self.minute == "":
                modal = Modal(
                    e, 
                    self.config.get_local_text("hey_modal_title"), self.config.get_local_text("you_must_choose_a_minute"),
                )
                modal.set_actions([
                        TextButton(self.config.get_local_text("modal_understood"), on_click=modal.close_dlg, style=ButtonStyle(color=REDEMPTION)),
                    ]
                )
                modal.open_dlg()
                return
            self.page = "chronometer"
            self.whileBreak = False
            func.visibler(self.timer_container, False)
            func.visibler(self.timer_stop_container, True)
            func.visibler(self.select_minute, False)
            func.visibler(self.minute_part, True)
            self.shield_container.content.content.color = REDEMPTION
            self.shield_container.update()
            self.settings_container.content.content.color = REDEMPTION
            self.settings_container.update()
            chrono = Chronometer(self.select_minute_dropdown.value)
            while True:
                result = chrono.chrono_counter()
                if self.whileBreak:
                    stop_click()
                    break
                if result == "time_is_up" or result[0] < 0 or result[1] < 0:
                    self.remaining_time.value = self.config.get_local_text("time_is_up")
                    self.remaining_time_container.update()
                    self.progressbar.value = None
                    self.progressbar_container.update()
                    self.percent.value = "%100"
                    self.percent_container.update()
                    self.whileBreak = True
                    if int(self.minute) == 3:
                        self.gold_bar.image_src = func.get_asset("0.08.png")
                    elif int(self.minute) == 6:
                        self.gold_bar.image_src = func.get_asset("0.16.png")
                    elif int(self.minute) == 9:
                        self.gold_bar.image_src = func.get_asset("0.24.png")
                    elif int(self.minute) == 12:
                        self.gold_bar.image_src = func.get_asset("0.32.png")
                    elif int(self.minute) == 15:
                        self.gold_bar.image_src = func.get_asset("0.36.png")
                    elif int(self.minute) == 20:
                        self.gold_bar.image_src = func.get_asset("0.40.png")
                    elif int(self.minute) == 25:
                        self.gold_bar.image_src = func.get_asset("0.44.png")
                    elif int(self.minute) == 30:
                        self.gold_bar.image_src = func.get_asset("0.48.png")
                    self.gold_bar.update()
                    if self.config.lastConfig["settings"]["task_completed_effect"]:
                        e.page.overlay[0].play()
                    break                
                if result[3] >= 30:
                    self.gold_bar.image_src = func.get_asset("0.48.png")
                elif result[3] >= 25:
                    self.gold_bar.image_src = func.get_asset("0.44.png")
                elif result[3] >= 20:
                    self.gold_bar.image_src = func.get_asset("0.40.png")
                elif result[3] >= 15:
                    self.gold_bar.image_src = func.get_asset("0.36.png")
                elif result[3] >= 12:
                    self.gold_bar.image_src = func.get_asset("0.32.png")
                elif result[3] >= 9:
                    self.gold_bar.image_src = func.get_asset("0.24.png")
                elif result[3] >= 6:
                    self.gold_bar.image_src = func.get_asset("0.16.png")
                elif result[3] >= 3:
                    self.gold_bar.image_src = func.get_asset("0.08.png")
                self.gold_bar.update()
                self.progressbar.value = result[2]*0.01
                self.percent.value = "%"+str(result[2])
                self.percent_container.update()
                self.progressbar_container.update()
                self.remaining_time.value = str(result[0]) + f" {self.config.get_local_text('minute')}, " + str(result[1]) + f" {self.config.get_local_text('second')}"
                self.remaining_time_container.update()
                sleep(1)
                        
        self.minute = ""
        
        self.select_minute_dropdown = Dropdown(
            on_change=select_minute_dropdown_change,
            label=self.config.get_local_text('task_minute'),
            hint_text=self.config.get_local_text('task_selection_hint_text'),
            filled=REDEMPTION,
            focused_border_color=REDEMPTION,
            label_style=TextStyle(color=WHITE, weight=FontWeight.BOLD),
            focused_bgcolor=BG,
            color=WHITE,
            text_style=TextStyle(color=WHITE, weight=FontWeight.BOLD),
            options=[
                dropdown.Option(text=self.config.get_local_text('3_minute'), key="3"),
                dropdown.Option(text=self.config.get_local_text('6_minute'), key="6"),
                dropdown.Option(text=self.config.get_local_text('9_minute'), key="9"),
                dropdown.Option(text=self.config.get_local_text('12_minute'), key="12"),
                dropdown.Option(text=self.config.get_local_text('15_minute'), key="15"),
                dropdown.Option(text=self.config.get_local_text('20_minute'), key="20"),
                dropdown.Option(text=self.config.get_local_text('25_minute'), key="25"),
                dropdown.Option(text=self.config.get_local_text('30_minute'), key="30"),
            ],
            autofocus=True,
        )
        
        self.select_minute = Column(
            visible=False,
            alignment="center",
            horizontal_alignment="center",
            spacing=90,
            controls=[
                self.select_minute_dropdown
            ]
        )
        
        self.languages = list()
        for langKey, value in self.config.lastConfig["languages"].items():
            self.languages.append(dropdown.Option(text=value["language_long_name"], key=str(langKey)))
            
        self.program_restart = Text(self.config.get_local_text('program_restart'), visible=False, color=REDEMPTION)
        
        self.settings = Column(
            visible=False,
            alignment="start",
            spacing=10,
            width=700,
            controls=[
                Row(
                    controls=[
                        Switch(
                            thumb_color=REDEMPTION if self.config.lastConfig["settings"]["sound_effects"] == True else WHITE,
                            inactive_thumb_color=FG, 
                            inactive_track_color=BG, 
                            track_color=BG,
                            value=self.config.lastConfig["settings"]["sound_effects"],
                            on_change=lambda e: settings_change(e, "sound_effects") 
                        ),
                        Text(self.config.get_local_text('sound_effects_settings'), size=17, weight=FontWeight.BOLD)
                    ]
                ),
                Row(
                    controls=[
                        Switch(
                            thumb_color=REDEMPTION if self.config.lastConfig["settings"]["task_completed_effect"] == True else WHITE,
                            inactive_thumb_color=FG, 
                            inactive_track_color=BG, 
                            track_color=BG,
                            value=self.config.lastConfig["settings"]["task_completed_effect"],
                            on_change=lambda e: settings_change(e, "task_completed_effect") 
                        ),
                        Text(self.config.get_local_text('task_completed_effect_settings'), size=17, weight=FontWeight.BOLD)
                    ]
                ),
                Row(
                    controls=[
                        Switch(
                            thumb_color=REDEMPTION if self.config.lastConfig["settings"]["discord_integration"] == True else WHITE,
                            inactive_thumb_color=FG, 
                            inactive_track_color=BG, 
                            track_color=BG,
                            value=self.config.lastConfig["settings"]["discord_integration"],
                            on_change=lambda e: settings_change(e, "discord_integration") 
                        ),
                        Text(self.config.get_local_text('discord_integration_settings'), size=17, weight=FontWeight.BOLD)
                    ]
                ),
                Row(
                    controls=[
                        Switch(
                            thumb_color=REDEMPTION if self.config.lastConfig["settings"]["discord_shield_password_view"] == True else WHITE,
                            inactive_thumb_color=FG, 
                            inactive_track_color=BG, 
                            track_color=BG,
                            value=self.config.lastConfig["settings"]["discord_shield_password_view"],
                            on_change=lambda e: settings_change(e, "discord_shield_password_view") 
                        ),
                        Text(self.config.get_local_text('discord_rpc_password_view'), size=17, weight=FontWeight.BOLD)
                    ]
                ),
                Dropdown(
                    on_change=language_dropdown_change,
                    label=self.config.get_local_text('language_dropdown_label'),
                    hint_text=self.config.get_local_text('language_long_name'),
                    filled=REDEMPTION,
                    focused_border_color=REDEMPTION,
                    label_style=TextStyle(color=WHITE, weight=FontWeight.BOLD),
                    focused_bgcolor=BG,
                    color=WHITE,
                    text_style=TextStyle(color=WHITE, weight=FontWeight.BOLD),
                    width=300,
                    options=self.languages,
                    autofocus=True
                ),
                self.program_restart
            ]
        )
        
        self.shield_password = TextField(
            label=self.config.get_local_text('lobby_password_label'),
            color=WHITE, 
            border_color=REDEMPTION,
            hint_text=self.config.get_local_text('lobby_password_hint_text'),
            label_style=TextStyle(color=WHITE, weight=FontWeight.BOLD),
            text_style=TextStyle(color=WHITE, weight=FontWeight.BOLD),
            focused_border_color=REDEMPTION,
            autofocus=True
        )
        
        if self.config.lastConfig["settings"]["shield_password"] is not None:
            self.shield_password.value = self.config.lastConfig["settings"]["shield_password"]
        
        if self.config.lastConfig["settings"]["shield_status"] == True:
            self.shield_password.disabled = True
        
        self.shield = Column(
            visible=False,
            alignment="center",
            horizontal_alignment="center",
            spacing=90,
            width=700,
            controls=[
                self.shield_password,
                Tooltip(
                    text_align="center",
                    message=self.config.get_local_text("shield_switch_tooltip"),
                    content=Switch(
                        thumb_color=REDEMPTION if self.config.lastConfig["settings"]["shield_status"] == True else WHITE,
                        inactive_thumb_color=FG, 
                        inactive_track_color=BG, 
                        track_color=BG,
                        value=self.config.lastConfig["settings"]["shield_status"],
                        on_change=shield_change
                    ),
                    padding=10,
                    border_radius=10,
                    text_style=TextStyle(size=10, color=colors.WHITE),
                )
            ]
        )
        
        self.progressbar = ProgressBar(width=700, bgcolor=BG, color=REDEMPTION)
        
        self.progressbar_container = Container(
            content=self.progressbar
        )
        
        self.remaining_time = Text(weight=FontWeight.BOLD, value=f"0 {self.config.get_local_text('minute')}, 0 {self.config.get_local_text('second')}", color=WHITE, size=17)
        
        self.remaining_time_container = Container(
            content=self.remaining_time
        )
        
        self.control_progressbar = ProgressBar(width=700, bgcolor=BG, color=REDEMPTION)
        
        self.control_progressbar_container = Container(
            content=self.control_progressbar
        )
        
        self.control_label = Text(weight=FontWeight.BOLD, value=self.config.get_local_text('controls_regressing'), color=WHITE, size=20)
        
        self.control_label_container = Container(
            content=self.control_label
        )
        
        self.percent = Text(weight=FontWeight.BOLD, value="%0.00", color=WHITE, size=17)
        
        self.percent_container = Container(
            content=self.percent
        )
        
        self.gold_bar = Container(
            width=220,
            height=150,
            image_src=Functions().get_asset("0.00.png"),
            image_fit=ImageFit.FILL,
        )
        
        self.minute_part = Column(
            visible=False,
            alignment="center",
            horizontal_alignment="center",
            spacing=30,
            controls=[
                self.gold_bar,
                Container(
                    padding=padding.only(left=20, right=20, bottom=0, top=0),
                    content=Row(
                        alignment="spaceBetween",
                        controls=[
                            self.remaining_time_container,
                            self.percent_container
                        ]    
                    )
                ),
                self.progressbar_container
            ]
        )
        
        self.control = Column(
            alignment="center",
            horizontal_alignment="center",
            spacing=30,
            controls=[
                Container(
                    padding=padding.only(left=20, right=20, bottom=0, top=0),
                    content=Row(
                        alignment="center",
                        controls=[
                            self.control_label_container,
                        ]    
                    )
                ),
                self.control_progressbar_container
            ]
        )
        
        self.timer_stop_container = Tooltip(
            visible=False,
            text_align="center",
            message=self.config.get_local_text('timer_stop_tooltip'),
            content=Container(
                width=50,
                bgcolor=REDEMPTION,
                border_radius=10,
                height=50,
                content=Icon(icons.STOP, color=WHITE),
                on_click=stop_click
            ),
            padding=10,
            border_radius=10,
            text_style=TextStyle(size=10, color=colors.WHITE),
        )
        
        self.timer_container = Tooltip(
            text_align="center",
            message=self.config.get_local_text('timer_start_tooltip'),
            content=Container(
                width=50,
                bgcolor=REDEMPTION,
                border_radius=10,
                height=50,
                content=Icon(icons.PLAY_ARROW, color=WHITE),
                on_click=start_click
            ),
            padding=10,
            border_radius=10,
            text_style=TextStyle(size=10, color=colors.WHITE),
        )
        
        self.shield_container = Tooltip(
            text_align="center",
            message=self.config.get_local_text('shield_tooltip'),
            content=Container(
                width=50,
                bgcolor=BG,
                border_radius=10,
                height=50,
                content=Icon(icons.SHIELD, color=WHITE),
                on_click=shield_click
            ),
            padding=10,
            border_radius=10,
            text_style=TextStyle(size=10, color=colors.WHITE),
        )
        
        self.settings_container = Tooltip(
            text_align="center",
            message=self.config.get_local_text('settings_tooltip'),
            content=Container(
                width=50,
                bgcolor=BG,
                border_radius=10,
                height=50,
                content=Icon(icons.SETTINGS, color=WHITE),
                on_click=settings_click
            ),
            padding=10,
            border_radius=10,
            text_style=TextStyle(size=10, color=colors.WHITE),
        )
                                
        self.rail = Container(
            visible=False,
            content=Row(
                alignment="center",
                controls=[
                    Container(
                        bgcolor=FG,
                        border_radius=10,
                        padding=10,
                        width=200,
                        content=Row(
                            spacing=10,
                            alignment="center",
                            controls=[
                                self.timer_stop_container,
                                self.timer_container,
                                self.shield_container,
                                self.settings_container
                            ]
                        )
                    )
                ]
            )
        )
        
        self.general_container = Container(
            height=490,
            border_radius=10,
            bgcolor=FG,
            content=Column(
                alignment="center",
                controls=[
                    self.control,
                    self.select_minute,
                    self.minute_part,
                    self.shield,
                    self.settings
                ]    
            ),
            padding=50
        )
        
        self.content = Container(
            alignment=alignment.center,
            content=Column(
                spacing=20,
                controls=[
                    self.general_container,
                    self.rail
                ]
            )
        )