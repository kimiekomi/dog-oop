#! /usr/bin/env python3

import time

debug = False
trace = True

class Timer:
    def __init__(self):
        if debug: print("constructed Timer class")

        self.timer_started = False


    def start(self):
        if debug: print("called start()")

        if self.timer_started:
            print("Timer already started")

        else:
            self.timer_started = True
            self.start_time = time.perf_counter()

            if trace: print(f"Start Time: {self.start_time:0.1f}")

    
    def check_time(self):
        if debug: print("called check_time()")

        if not self.timer_started:
            print("Timer has NOT started")

        else:
            self.current_time = time.perf_counter()
            print(f"Current Time: {self.current_time:0.1f}")

            return self.current_time


    def stop(self):
        if debug: print("called stop()")

        if not self.timer_started:
            print("Timer has NOT started")

        else:
            self.stop_time = time.perf_counter()
            self.timer_started = False

            if trace: print(f"Stop Time: {self.stop_time:0.1f}")

    
    def elapsed_time(self):
        if debug: print("called elapsed_time()")

        if not self.timer_started:
            print("Timer has NOT started")

        else:
            self.stop_time = time.perf_counter()
            self.total_time = self.stop_time - self.start_time

            if trace: print(f"Elapsed Time: {self.total_time:0.1f} seconds")

        return self.total_time


if __name__ == "__main__":
    timer = Timer()
   
    # time.sleep(2)
    # timer.start()
    # time.sleep(1)
    # timer.stop()
    # timer.check_time()
    # time.sleep(1)
    # timer.start()
    # timer.check_time()
    # time.sleep(2)
    # timer.stop()

    # timer.start()
    # time.sleep(2)
    # timer.start()

    time.sleep(2)
    timer.start()
    time.sleep(1)
    timer.elapsed_time()
    time.sleep(1)
    timer.stop()

