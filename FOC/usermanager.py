######################################
# User Manager Version 1.0.0         #
# by @TRC-Loop                       #  
# (C) 2022 TRC Loop - MIT License    #
#____________________________________#
# Tools used:                        #
# OpenAI ChatGPT                     #
# Github Copilot                     #
# Python 3.11.1                      #
######################################

# Just for info, this is the first version of the user manager. It is not complete, but it is a start. I will be adding more to it in the future.
# The Usermanager uses JSONX files to save data. These files are the exacly same as JSON files. The only difference is the Filename.
# If you want Syntax highliting for jsonx files in VSCode, do these Steps:
# 1. Open the Command Palette (Ctrl+Shift+P)
# 2. Type "change Language Mode"
# 3. click on "Configure File Association for .jsonx"
# 4. Type "json" in the "Language" field and select JSON or JSON with Comments.
# 5. Done!
import os
import json
import hashlib
import requests
import time
import getpass
import datetime



class UserManager:
    def __init__(self):
        self.base_path = "users"

        # Create the data directory if it doesn't exist
        if not os.path.exists(self.base_path):
            os.makedirs(self.base_path)

    def load_user(self, userName):
        file_path = os.path.join(self.base_path, userName, "data", "user", "user.jsonx")
        if not os.path.exists(file_path):
            return None

        with open(file_path, "r") as f:
            return json.load(f)
        
        

    def save_user(self, username, user_data):
        user_path = os.path.join(self.base_path, username)
        if not os.path.exists(user_path):
            os.makedirs(user_path)

        file_path = os.path.join(user_path, "user.jsonx")
        with open(file_path, "w") as f:
            json.dump(user_data, f, indent=4)

    def add_user(self, username, password, passhint = "", permission_level = 2, info = "", email = "", phone = "", fullname = "", birthdate = "", address = "", city = "", state = "", zipcode = "", country = "", system = False, installer = False, program = False, user = True):
        
        # Create user directory
        user_path = os.path.join(self.base_path, username)
        if os.path.exists(user_path):
            raise FileExistsError("User already exists")
            return
        os.makedirs(user_path)

        # Create subdirectories
        os.makedirs(os.path.join(user_path, "data", "User"))
        os.makedirs(os.path.join(user_path, "data", "Settings"))
        os.makedirs(os.path.join(user_path, "data", "Programs"))
        os.makedirs(os.path.join(user_path, "data", "System", "Dictonaries"))
        os.makedirs(os.path.join(user_path, "home"))
        os.makedirs(os.path.join(user_path, "downloads"))
        os.makedirs(os.path.join(user_path, "programs"))
        os.makedirs(os.path.join(user_path, "access"))
        os.makedirs(os.path.join(user_path, "videos"))
        os.makedirs(os.path.join(user_path, "pictures"))
        os.makedirs(os.path.join(user_path, "encrypted"))
        os.makedirs(os.path.join(user_path, "documents"))
        os.makedirs(os.path.join(user_path, "other"))
        os.makedirs(os.path.join(user_path, "bin"))
        # Save user info in JSON file
        if permission_level >= 4:
            permission_level = 4
            
        if permission_level == 4:
            system = True
            
            
        user_info = {
            "username": username,
            "password_hash": self.hash_password(password),
            "password_hint": passhint,
            "permission_level": permission_level,
            "info": info,
            "email": email,
            "phone": phone,
            "fullname": fullname,
            "birthdate": birthdate,
            "address": address,
            "city": city,
            "state": state,
            "zipcode": zipcode,
            "country": country,
            "system": system,
            "installer": installer,
            "program": program,
            "user": user,
            "created": str(datetime.datetime.now()),
        }
        with open(os.path.join(user_path, "data", "User", "user.jsonx"), "w") as f:
            json.dump(user_info, f, indent=4)
            
        # Permission Dictonary
        Dict_Permissions = {
            "Level0": "No Access",
            "Level1": "Read Only",
            "Level2": "Read/Write (Non-Admin) (User Standard)",
            "Level3": "Read/Write (Admin)",
            "Level3.1": "Read/Write (Admin) (Installer Standard)",
            "Level3.2": "Read/Write (Admin) (Program Standard)",
            "Level4": "Super Admin (System) Can change other Permission levels",
            "Higher": "Like Level 4",
        }
        with open(os.path.join(user_path, "data", "System", "Dictonaries", "Permissions.jsonx"), "w") as f:
            json.dump(Dict_Permissions, f, indent=4)
            
        # Filetype Dictonary
        Dict_Filetypes = {
            ".jsonx": "JSON tl+ confiuration file",
            ".mp4": "Video file",
            ".mp3": "Audio file",
            ".wav": "Audio file",
            ".exe": "Executable file",
            ".zip": "Compressed file",
            ".rar": "Compressed file",
            ".7z": "Compressed file",
            ".tar": "Compressed file",
            ".gz": "Compressed file",
            ".iso": "Disk image file",
            ".bin": "Binary File",
            ".dat": "data file",
            ".db": "Database file",
            ".log": "Log file",
            ".xml": "XML file",
            ".html": "HTML file",
            ".css": "CSS file",
            ".js": "JavaScript file",
            ".py": "Python file",
            ".c": "C file",
            ".cpp": "C++ file",
            ".cs": "C# file",
            ".java": "Java file",
            ".jar": "Java Archive file",
            ".sh": "Shell file",
            ".bat": "Batch file",
            ".vb": "Visual Basic file",
            ".ps1": "PowerShell file",
            ".php": "PHP file",
            ".asp": "ASP file",
            ".aspx": "ASPX file",
            ".sql": "SQL file",
            ".csv": "CSV file",
            ".tsv": "TSV file",
            ".ods": "OpenDocument Spreadsheet",
            ".odt": "OpenDocument Text",
            ".rtf": "Rich Text Format",
            ".wks": "Works Spreadsheet",
            ".wps": "Works Text",
            ".wpd": "WordPerfect Document",
            ".key": "Keynote Presentation",
            ".odp": "OpenDocument Presentation",
            ".pps": "PowerPoint Slide Show",
            ".ppt": "PowerPoint Presentation",
            ".pptx": "PowerPoint Presentation X",
            ".cbr": "Comic Book RAR Archive",
            ".cbz": "Comic Book ZIP Archive",
            ".cb7": "Comic Book 7-Zip Archive",
            ".cbt": "Comic Book TAR Archive",
            ".cba": "Comic Book ACE Archive",
            ".cbt": "Comic Book TAR Archive",
            ".epub": "Electronic Publication",
            ".fb2": "FictionBook 2.0",
            ".ibooks": "iBooks Author Publication",
            ".lit": "Microsoft Reader eBook",
            ".mobi": "Mobipocket eBook",
            ".opf": "Open Publication Format",
            ".pdb": "Palm Database eBook",
            ".pdf": "Portable Document Format",
            ".prc": "Palm Resource eBook",
            ".azw": "Amazon Kindle eBook",
            ".azw3": "Amazon Kindle eBook",
            ".kf8": "Amazon Kindle eBook",
            ".kfx": "Amazon Kindle eBook",
            ".snb": "Sony Reader eBook",
            ".ttf": "TrueType Font",
            ".otf": "OpenType Font",
            ".fnt": "Windows Font",
            ".fon": "Generic Font",
            ".woff": "Web Open Font Format",
            ".eot": "Embedded Open Type Font",
            ".pfb": "PostScript Font Binary",
            ".pfm": "PostScript Font Metrics",
            ".afm": "Adobe Font Metrics",
            ".ai": "Adobe Illustrator File",
            ".psd": "Adobe Photoshop Document",
            ".indd": "Adobe InDesign Document",
            ".pct": "Mac Pict",
            ".pict": "Mac Pict",
            ".bmp": "Bitmap Image",
            ".dib": "Bitmap Image",
            ".gif": "Graphics Interchange Format",
            ".jpg": "JPEG Image",
            ".jpeg": "JPEG Image",
            ".jpe": "JPEG Image",
            ".jp2": "JPEG 2000 Image",
            ".j2k": "JPEG 2000 Image",
            ".jpf": "JPEG 2000 Image",
            ".jpx": "JPEG 2000 Image",
            ".jpm": "JPEG 2000 Image",
            ".mj2": "JPEG 2000 Image",
            ".mjp2": "JPEG 2000 Image",
            ".png": "Portable Network Graphics",
            ".ps": "PostScript File",
            ".svg": "Scalable Vector Graphics",
            ".tif": "Tagged Image File Format",
            ".tiff": "Tagged Image File Format",
            ".cr2": "Canon Raw 2 Image",
            ".nrw": "Nikon Raw Image",
            ".orf": "Olympus Raw Image",
            ".raf": "Fuji Raw Image",
            ".arw": "Sony Raw Image",
            ".dng": "Digital Negative Image",
            ".3fr": "Hasselblad Raw Image",
            ".srf": "Sony Raw Image",
            ".sr2": "Sony Raw Image",
            ".kdc": "Kodak Raw Image",
            ".dcr": "Kodak Raw Image",
            ".erf": "Epson Raw Image",
            ".mef": "Mamiya Raw Image",
            ".ptx": "Pentax Raw Image",
            ".pef": "Pentax Raw Image",
            ".r3d": "Red Raw Image",
            ".x3f": "Sigma Raw Image",
            ".srw": "Samsung Raw Image",
            ".rw2": "Panasonic Raw Image",
            ".raw": "Raw Image",
            ".doc": "Microsoft Word Document",
            ".docx": "Microsoft Word Document X",
            ".dot": "Microsoft Word Document Template",
            ".dotx": "Microsoft Word Document Template X",
            ".docm": "Microsoft Word Document Macro",
            ".dotm": "Microsoft Word Document Template Macro",
            ".wps": "Microsoft Works Document",
            ".wks": "Microsoft Works Spreadsheet",
            ".wpd": "WordPerfect Document",
            ".rtf": "Rich Text Format",
            ".txt": "Text File",
            ".excel": "Microsoft Excel Spreadsheet",
            ".xlsx": "Microsoft Excel Spreadsheet X",
            ".xls": "Microsoft Excel Spreadsheet",
            ".xlsm": "Microsoft Excel Spreadsheet Macro",
            ".xlsb": "Microsoft Excel Spreadsheet Binary",
            ".xlt": "Microsoft Excel Spreadsheet Template",
            ".xltm": "Microsoft Excel Spreadsheet Template Macro",
            ".xltx": "Microsoft Excel Spreadsheet Template X",
            ".numbers": "Apple Numbers Spreadsheet",
            ".json": "JSON File",

        }
        with open(os.path.join(user_path, "data", "System", "Dictonaries", "Filetypes.jsonx"), "w") as f:
            json.dump(Dict_Filetypes, f, indent=4)
            
        Dict_English1 = requests.get("https://raw.githubusercontent.com/matthewreagan/WebstersEnglishDictionary/master/dictionary.json")
        Dict_English2 = Dict_English1.json()
        with open(os.path.join(user_path, "data", "System", "Dictonaries", "English.jsonx"), "w") as f:
            json.dump(Dict_English2, f, indent=4)
            
            
    def verify_password(self, username, password):
        user_data = self.load_user(username)
        if not user_data:
            return False
        return user_data["password_hash"] == self.hash_password(password)

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def prompt_password(self, username, use_hint = True):
        wait_time = 1
        tries = 0
        while True:
            password = getpass.getpass(f"Enter password for {username}: ")
            if self.verify_password(username, password):
                print("Welcome, " + username + ".")
                return
            else:
                print("Incorrect password. Please try again.")
                time.sleep(wait_time)
                wait_time += 1
                if use_hint:
                    tries += 1
                if use_hint and tries >= 3:
                    print(f"Hint: {self.load_user(userName=username)['password_hint']}")
                
