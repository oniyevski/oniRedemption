from datetime import datetime, timedelta

class Chronometer:
    def __init__(self, goldMinute):
        self.goldMinute = datetime.now() + timedelta(minutes=int(goldMinute)) 
        self.totalSecond = int((self.goldMinute - datetime.now()).total_seconds())
        self.total = self.totalSecond
        self.start = datetime.now()
        self.counter = 0
        
    def chrono_counter(self):
        if self.totalSecond > 0:
            self.totalSecond -= 1
            lastSecond = int((self.goldMinute - datetime.now()).total_seconds())
            minute, second = divmod(lastSecond, 60)
            if self.counter < self.total:
                self.counter += 1
            return minute, second, float(f"{self.counter/self.total * 100:.2f}"), int((datetime.now() - self.start).seconds/60)
        else:
            return "time_is_up"
