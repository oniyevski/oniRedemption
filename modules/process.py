import psutil, subprocess


class Process:
    def __init__(self, process):
        self.process = process

    def getProcessStatus(self) -> str:
        try:
            for proc in psutil.process_iter():
                if proc.name() == self.process:
                    return proc.cwd()
            return "stopped"
        except:
            return "error"

    def stopProcess(self):
        try:
            getStatus = self.getProcessStatus()
            if getStatus != "stopped" and getStatus != "error":
                subprocess.check_output(f"taskkill /im {self.process}", shell=False, stderr=subprocess.STDOUT)
                return "stopped"
            else:
                return "error"
        except:
            return "error"