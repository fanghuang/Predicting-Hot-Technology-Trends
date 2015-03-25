from plan import Plan

cron = Plan()

cron.command('python /vagrant/stackoverflow.py', every='1.day', at='12:05')


if __name__ == '__main__':
    cron.run('write')