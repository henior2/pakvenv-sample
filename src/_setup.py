import os
import sys

# add pakenv's start.py to crontab on boot
def add_to_crontab():
	import crontab
	cron = crontab.CronTab(user=os.getlogin()) if sys.platform == "win32" else crontab.CronTab(user=True)
	job = cron.new(command=f"{sys.executable} {os.path.join(os.getcwd(), 'start.py')}")
	job.set_comment("pakenv at " + os.getcwd())
	job.every_reboot()
	cron.write()

# add_to_crontab()