import os
import time

def read_count():
    try:
        with open("./count.txt", 'r', encoding="utf8") as f:
            return int(f.read().strip())
    except (FileNotFoundError, ValueError):
        return 1

def save_count(n):
    with open("./count.txt", 'w', encoding="utf8") as f:
        f.write(str(n))

def auto_commit():
    n = read_count()
    f = open("./count.txt", 'a', encoding="utf8")
    f.write(" ")
    
    os.system("git add count.txt")
    os.system("git commit -m \"This is an automated commit.\"")
    os.system("git push origin main")
    
    n+=1
    save_count(n)


while True:
    auto_commit()
    print(f"Loop {read_count()}")
    time.sleep(24/60/60)