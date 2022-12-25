from sys import platform
import pyperclip, wave

class Clipboard:
    
    def Clear() -> None:
        if platform == "linux" or platform == "linux2":
            pyperclip.copy("")
        elif platform == "darwin":
            pyperclip.copy("")
        elif platform == "win32":
            pyperclip.copy("")
            from ctypes import windll
            if windll.user32.OpenClipboard(None):
                windll.user32.EmptyClipboard()
                windll.user32.CloseClipboard()

    def ContainsAudio() -> bool:
        raise SystemError("Clipboard currently only supports text")
    
    def ContainsData(dataType: str) -> bool:
        raise SystemError("Clipboard currently only supports text")

    def ContainsFileDropList() -> bool:
        raise SystemError("Clipboard currently only supports text")

    def ContainsImage() -> bool:
        raise SystemError("Clipboard currently only supports text")

    def ContainsText() -> bool:
        if pyperclip.paste() != "":
            return True
        else:
            return False
    
    def ContainsText(TextDataFormat) -> bool:
        raise SystemError("Clipboard currently only supports text")
    
    def Flush() -> None:
        raise SystemError("Currently not supported by Clipboard")

    def GetAudioStream() -> bytes:
        raise SystemError("Clipboard currently only supports text")

    def GetData(String) -> bytes:
        raise SystemError("Clipboard currently only supports text")
        
    def GetDataObject() -> bytes:
        raise SystemError("Clipboard currently only supports text")

    def GetFileDropList() -> list:
        raise SystemError("Clipboard currently only supports text")

    def GetImage() -> bytes:
        raise SystemError("Clipboard currently only supports text")

    def GetText(TextDataFormat = "") -> str:
        return pyperclip.paste()

    def IsCurrent(IDataObject) -> bool:
        raise SystemError("Clipboard currently only supports text")

    def SetAudio(ByteOrStream) -> None:
        raise SystemError("Clipboard currently only supports text")

    def SetData(String, Object) -> None:
        raise SystemError("Clipboard currently only supports text")
    
    def SetDataObject(Object, Boolean = True) -> None:
        raise SystemError("Clipboard currently only supports text")

    def SetFileDropList(StringCollection) -> None:
        raise SystemError("Clipboard currently only supports text")

    def SetImage(BitmapSource) -> None:
        raise SystemError("Clipboard currently only supports text")

    def SetText(String, TextDataFormat = "") -> None:
        pyperclip.copy(String)
