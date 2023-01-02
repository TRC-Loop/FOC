import loglib
from loglib import json

# Open config file for colorcodes for the logger
try:
    with open('colors.jsonx', 'r') as f:
        color_config = json.load(f)
except:
    # Create the file
    with open('colors.jsonx', 'w') as f:
        json.dump({
            "info": "[green]",
            "warning": "[yellow]",
            "error": "[red]",
            "fatal": "[bold red]",
            "time": "[bold blue]",
        }, f, indent=4)
    with open('colors.jsonx', 'r') as f:
        color_config = json.load(f)


log = loglib.Logger(['error', 'fatal'], color_config)
log.log_info("Importing Modules")
try:
    import loglib
    log.log_warning("Imported Loglib ! Already imported.")
except ImportError or ImportWarning:
    log.log_info("Loglib running good. continueing...")

log.log_info("Importing CMD")
import cmd
log.log_info("Importing OS")
import os
log.log_info("Importing SYS")
import sys
log.log_info("Importing TIME")
import time
log.log_info("Importing DATETIME")
import datetime
log.log_info("Importing JSON")
import json
log.log_info("Importing RICH [")
import rich
log.log_info("Importing RICH PRINT")
from rich import print
log.log_info("Importing RICH TABLE")
from rich import table
log.log_info("Importing RICH CONSOLE")
from rich import console
log.log_info("Importing RICH PANEL")
from rich import panel
log.log_info("Importing RICH PROGRESS")
from rich import progress
log.log_info("Importing RICH TRACEBACK")
from rich import traceback
log.log_info("Importing RICH LIVE")
from rich import live
log.log_info("Importing RICH MARKDOWN")
from rich import markdown
log.log_info("Importing RICH PRETTY")
from rich import pretty
log.log_info("Importing RICH JSON")
from rich import json, print_json
log.log_info("Importing RICH TREE")
from rich import tree
log.log_info("Importing RICH INSPECT")
from rich import inspect
log.log_info("Importing RICH SYNTAX")
from rich import syntax
log.log_info("Importing RICH BOX")
from rich import box
log.log_info("Importing RICH MEASURE")
from rich import measure
log.log_info("Importing RICH BAR")
from rich import progress_bar, bar
log.log_info("Importing RICH SPINNER ]")
from rich import spinner
log.log_info("Importing ARGPARSE")
import argparse
log.log_info("Importing SUBPROCESS")
import subprocess
log.log_info("Importing SHUTIL")
import shutil
log.log_info("Importing GETPASS")
import getpass
log.log_info("Importing PLATFORM")
import platform
log.log_info("Importing SOCKET")
import socket


log.log_info("--Importing Builtins (FOC)--")
log.log_info("Importing USERMANAGER .py")
import usermanager
log.log_info("Importing [dotpy BETA]MY .py")
import My
log.log_info("Importing [dotpy BETA]SYSTEM .py")
import System


log.log_info("Setting up variables")
mgr = usermanager.UserManager()

log.log_info("Defining needed Functions")


log.log_info("Defining argparser")
def argparser(arguments, arg, needed: bool):
    log.log_info("argparser() got executed: args: argument: " + arguments + ", arg: " + arg + ", needed: " + needed)
    log.log_info("splitting arguments")
    args_list = arguments.split()
    
    # Extract the value of the --string parameter
    log.log_info("Extracting the value of the -- parameter")
    string_value = None
    for i in range(len(args_list)):
        if args_list[i] == '--' + arg:
            log.log_info("Found the value of the -- parameter")
            string_value = args_list[i+1]
            break
    
    # Print the value of the --string parameter
    if needed:
        if not string_value:
            print(f'--{arg} was not found.')
            log.log_error("--" + arg + " was not found.")
            return False
    else:
        log.log_info("finished exuting. returning string_value")
        return string_value
    
log.log_info("Initalizating Console/Shell/CMD LIB, Classname: FOConsole")











class FOConsole(cmd.Cmd):
    def __init__(self, username: str):
        super().__init__()
        self.path = os.getcwd()
        self.computer_name = socket.gethostname()
        self.username = username

    def prompt(self):
        self.path = os.getcwd()
        return f"{self.username.lower()}@{self.computer_name.lower()}:{self.path}// "

    def cmdloop(self, intro=None): # for prompt
        """Override the cmdloop method to manually call the prompt method"""
        print(self.prompt(), end=' ')
        line = self.stdin.readline()
        while line:
            self.onecmd(line)
            print(self.prompt(), end=' ')
            line = self.stdin.readline()









if __name__ == '__main__':
    log.log_info("__name__ == __main__ got executed")
    log.log_info("Asking for user info")
    username = input("Username: ")
    try:
        log.log_info("Asking for password")
        mgr.prompt_password(username, True)
        log.log_info("Password correct: ")
    except:
        print("[red bold]User not found.")
        log.log_fatal("User: " + username + "not found.")
    log.log_info("Loading Console")
    FOC = FOConsole(username)
    log.save_log("latest.log")
    log.log_info("Running Console")
    FOC.cmdloop()
    log.log_info("Unexcepted Close, 0.1.")