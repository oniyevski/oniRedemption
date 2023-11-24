from flet import *

class Modal:
    def __init__(self, e, title, message, actions=None) -> None:
        self.e = e
        self.dlg_modal = AlertDialog(
            modal=True,
            title=Text(title),
            content=Text(message),
            actions_alignment=MainAxisAlignment.END
        )
        if actions is not None:
            for action in actions:
                self.dlg_modal.actions.append(action)
                
    def close_dlg(self, event=None):
        self.dlg_modal.open = False
        self.e.page.update()
        
    def open_dlg(self):
        self.e.page.dialog = self.dlg_modal
        self.dlg_modal.open = True
        self.e.page.update()
        
    def set_actions(self, actions=None):
        if actions is not None:
            for action in actions:
                self.dlg_modal.actions.append(action)