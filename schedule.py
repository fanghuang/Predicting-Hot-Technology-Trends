from plan import Plan

cron = Plan()

cron.command('python /vagrant/stackoverflow.py', every='1.day', at='12:05')
cron.command('python /vagrant/sendEmail.py', every='1.week')


if __name__ == '__main__':
    cron.run('write')
