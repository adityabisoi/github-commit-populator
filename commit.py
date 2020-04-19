import subprocess
import write
import random
import time

while True:
    time.sleep(86400)
    for _ in range(random.randint(1,3)):
        text = random.randint(0,99999)
        write.write("file.txt",text)
        subprocess.run('git add file.txt', shell=True)
        subprocess.run('git commit -m "new commit"', shell=True)
        subprocess.run('git push', shell=True)