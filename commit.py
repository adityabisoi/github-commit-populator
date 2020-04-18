import subprocess
import write
import random
import time

text = random.randint(0,99999)
write.write("file.txt",text)
time.sleep(1)
subprocess.run('git add file.txt', shell=True)