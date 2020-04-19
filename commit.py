import subprocess
import write
import random
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-sun', hour=10)
def scheduled_job():
    for _ in range(random.randint(1,3)):
        text = random.randint(0,99999)
        write.write("file.txt",text)
        subprocess.run('git add file.txt', shell=True)
        subprocess.run('git commit -m "new commit"', shell=True)
        subprocess.run('git push', shell=True)

sched.start()