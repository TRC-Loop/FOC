import os, sys, shutil, random

class Presets:
    LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
    UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    NUMBERS = "0123456789"
    SYMBOLS = "!§$%&\\()=?\"'#+-.,;:_*~ß<>|[}]{/"
    BRACKETS = "()[]{}"
class IO:
    class File:
        def exists(file: str) -> bool:
            if os.path.exists(file):
                return True
            elif not os.path.exists(file):
                return False
            else:
                raise RuntimeError
            
        def create(file: str) -> None:
            with open(file, "a"):
                pass
            
        def write(file: str, text: str) -> None:
            with open(file, "w") as f:
                f.write(text)
                
        def writeBytes(file: str, text: str) -> None: 
            with open(file, "wb") as f:
                f.write(text)
                
        def writeAppend(file: str, text: str) -> None:
            with open(file, "a") as f:
                f.write(text)
            
        def read(file: str) -> str:
            with open(file, "r") as f:
                readText = f.read()
            return readText
        
        def delete(file: str) -> None:
            os.remove(file)
        
        def rename(file: str, newname: str) -> None:
            os.rename(file, newname)
            
        def move(file: str, to: str) -> None:
            shutil.move(file, to)
            
        def copy(file: str, to: str) -> None:
            shutil.copy(file, to)
            
    class Directory:
        def exists(dir: str) -> bool:
            if os.path.isdir(dir):
                return True
            elif os.path.isdir(dir):
                return False
            else:
                raise RuntimeError
        
        def create(dir: str) -> None:
            os.mkdir(dir)
            
        def delete(dir: str) -> None:
            os.rmdir(dir)
            
        def rename(dir: str, dirname: str) -> None:
            os.rename(dir, dirname)
            
        def deleteRecursive(dir: str) -> None:
            shutil.rmtree(dir)

        def move(dir: str, to: str) -> None:
            shutil.move(dir, to)
            
        def copy(dir: str, to: str) -> None:
            shutil.copy(dir, to)

class Random:
    def randomRange(start: int, end: int) -> int:
        return random.randrange(start, end)
    
    def randomInt(start: int, end: int) -> int:
        return random.randint(start, end)
    
    def randomString(length: int = 8, sequence: str = Presets.LOWERCASE + Presets.UPPERCASE + Presets.NUMBERS) -> str:
        return "".join(random.choice(sequence) for i in range(length))
    
    def randomBytes(count: int = 8) -> bytes:
        return random.randbytes(count)