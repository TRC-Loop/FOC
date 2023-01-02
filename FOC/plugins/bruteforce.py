import itertools
import time
def check_password(password):
  # Hier würde man das Passwort ausprobieren und überprüfen,
  # ob es das gesuchte Passwort ist
  # zum Beispiel indem man es mit einem Passwort aus einer Datenbank vergleicht
  return password == '99zz';

def bruteforce(chars, length=None, logprint=False):
    # Start to read runtime
    start = time.time()
    if length is None:
        length = 1;
    while True:
        for attempt in itertools.product(chars, repeat=length):
            attempt_str = ''.join(attempt)
            if logprint: print(attempt_str, end='\r');       
            if check_password(attempt_str):
                stop = time.time()
                runned = stop - start
                return attempt_str, runned;
        length += 1;
    else:
        for attempt in itertools.product(chars, repeat=length):
            attempt_str = ''.join(attempt);
            if logprint: print(attempt_str, end='\r');
            if check_password(attempt_str):
                return attempt_str;

    return 'Password not found';

# Beispielaufruf ohne Angabe der Länge
result = bruteforce('abcdefghijklmnopqrstuvwxyz0123456789', 4, True)
print(result[0])
print(round(result[1], 3))