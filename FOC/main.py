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
            "error": "#[red]",
            "fatal": "#[bold red]}",
            "time": "[bold blue]",
        }, f, indent=4)
    with open('colors.jsonx', 'r') as f:
        color_config = json.load(f)


log = loglib.Logger(["info", 'warning', 'error', 'fatal'], color_config)
log.log_info("Hello, world!")
log.save_log("latest.log")