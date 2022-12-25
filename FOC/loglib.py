import json
import datetime
from rich import print





class Logger:
    def __init__(self, log_levels: list, color_config: dict):
        self.log_levels = log_levels
        self.color_config = color_config
        self.log_entries = ""
    def log(self, message: str, log_level: str):
        if log_level not in self.log_levels:
            raise ValueError(f"Invalid log level: {log_level}")
        current_time = str(datetime.datetime.now())
        log_string = f'[{log_level.upper()}] {message}'
        log_time = f"[{current_time}]"
        log_entry = f"{log_time} {log_string}"
        log_print = f"{self.color_config['time']}{log_time} {self.color_config[log_level]}{log_string}"
        print(log_print)
        self.log_entries += log_entry + "\n"
    def save_log(self, filename: str):
        with open(filename, 'w') as f:
            f.write(self.log_entries)
    
    def load_log(self, filename: str):
        with open(filename, 'r') as f:
            self.log_entries = f.read()
    
    def log_info(self, message: str):
        self.log(message, 'info')
    
    def log_warning(self, message: str):
        self.log(message, 'warning')
    
    def log_error(self, message: str):
        self.log(message, 'error')
    
    def log_fatal(self, message: str):
        self.log(message, 'fatal')
