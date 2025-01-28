import time

class Timer:
    def __init__(self):
        self.start_time = None
        self.end_time = None
    
    def start(self):
        self.start_time = time.time()
        print("Timer started.")
    
    def stop(self):
        if self.start_time is None:
            print("Timer hasn't started yet.")
        else:
            self.end_time = time.time()
            print("Timer stopped.")
    
    def duration(self):
        if self.start_time is None:
            print("Timer hasn't started yet.")
            return None
        elif self.end_time is None:
            print("Timer hasn't stopped yet.")
            return None
        else:
            return self.end_time - self.start_time
    
    def display_duration(self):
        duration = self.duration()
        if duration is not None:
            print(f"Duration: {duration:.2f} seconds")


timer1 = Timer()
timer1.start()

time.sleep(2)  

timer1.stop()
timer1.display_duration()
