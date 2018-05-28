#!/usr/bin/env python3

# Checks two websites for updates

# imports
import requests
import bs4
import smtplib
import schedule
import time
import logging
import os


# Setting up Logger
logFormatter = logging.Formatter('%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s')
log = logging.getLogger()

logPath = os.getcwd()
logName = 'HousingDevScraper'

fileHandler = logging.FileHandler('{0}/{1}.log'.format(logPath, logName))
fileHandler.setFormatter(logFormatter)
log.addHandler(fileHandler)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
log.addHandler(consoleHandler)

log.setLevel(logging.INFO)

log.info('Script Initiated')
log.info('Logfile is {}\\{}.log\n'.format(logPath, logName))


# vars
passNumber = 1


def main():
    urls = [r'https://www.huntingtonbeachca.gov/government/departments/planning/major/major-projects-view.cfm?ID=66',
            r'https://www.huntingtonbeachca.gov/government/departments/planning/major/major-projects-view.cfm?ID=67'
            ]
    for url in urls:
        log.info('Checking {}'.format(url))
        res = requests.get(url)
        res.raise_for_status()

        log.info('Download Complete')

        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        pElems = soup.select('p')

        for i in pElems:
            if 'Project Status' in i.getText():
                if 'Plan Check' not in i.getText():
                    log.info('Change found. Sending email.')
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login('EMAIL', 'PW')
                    subject = 'Housing Change in Huntington Beach'
                    text = 'The housing plan in huntington beach has been updated. \n{}'.format(url)
                    msg = 'Subject: {}\n\n{}'.format(subject, text)
                    server.sendmail('EMAIL', 'EMAIL', msg)
                    server.sendmail('EMAIL', 'EMAIL', msg)
                    server.quit()
                else:
                    log.info('No change found.\n')

if __name__ == '__main__':
    main()


# Scheduling options
schedule.every().hour.do(main)

# Alternate scheduling options
# schedule.every(10).minutes.do(main)
# schedule.every().day.at('10:30').do(main)

# Setting perpetual schedule
while True:
    log.info('Running script pass number {}'.format(passNumber))
    passNumber += 1
    schedule.run_pending()
    time.sleep(60) # wait one minute

# Optional No hangup backgroud run with output to nohup.out
# nohup python2.7 -u HousingDevScaper.py &