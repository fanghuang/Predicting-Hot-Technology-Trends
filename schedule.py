from plan import Plan

cron = Plan()

cron.command('python ~/PHTT/linkedin.py', every='1.day', at='12:00')
cron.command('python ~/PHTT/stackoverflow.py', every='1.day', at='12:05')


if __name__ == '__main__':
    cron.run('write')