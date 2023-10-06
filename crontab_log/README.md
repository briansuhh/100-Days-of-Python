## How to make a Crontab Jobs

- the 5 stars are the time on which the job will run
- the last part is the command to run

```bash
# make a crontab jobs
crontab -e

# Edit this file to introduce tasks to be run by cron.
# 
# Each task to run has to be defined through a single line
# indicating with different fields when the task will be run
# and what command to run for the task
# 
# To define the time you can provide concrete values for
# minute (m), hour (h), day of month (dom), month (mon),
# and day of week (dow) or use '*' in these fields (for 'any').
# 
# Notice that tasks will be started based on the cron's system
# daemon's notion of time and timezones.
# 
# Output of the crontab jobs (including errors) is sent through
# email to the user the crontab file belongs to (unless redirected).
# 
# For example, you can run a backup of all your user accounts
# at 5 a.m every week with:
# 0 5 * * 1 tar -zcf /var/backups/home.tgz /home/
# 
# For more information see the manual pages of crontab(5) and cron(8)
# 
# m h  dom mon dow   command
* * * * * python3 '/mnt/d/Files/Programming/100 Days of Code Python/Day 33/sunrise_sunset/main.py'       
* * * * * python3 '/mnt/d/Files/Programming/100 Days of Code Python/crontab_log/main.py'

# show all the crontab jobs
crontab -l

# restart the crontab service
sudo service cron restart
```