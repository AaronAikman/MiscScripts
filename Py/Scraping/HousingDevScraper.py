# Checks two websites for updates

import requests, bs4, datetime, smtplib
import logging

import schedule
import time


logging.basicConfig(filename='Tracker.log',level=logging.DEBUG)


def main():
    urls = [r'https://www.huntingtonbeachca.gov/government/departments/planning/major/major-projects-view.cfm?ID=66',
            r'https://www.huntingtonbeachca.gov/government/departments/planning/major/major-projects-view.cfm?ID=67'
            ]
    for url in urls:
        logging.info('Checking {}'.format(url))
        print('Checking {}'.format(url))
        res = requests.get(url)
        res.raise_for_status()

        print('Download completed at {}'.format(datetime.datetime.now()))
        logging.info('Download Complete')
        soup = bs4.BeautifulSoup(res.text, "html.parser")

        print('soup complete')
        logging.info('Soup Complete')

        pElems = soup.select('p')
        for i in pElems:
            if 'Project Status' in i.getText():
                if 'Plan Check' not in i.getText():
                    logging.info('Change found!')
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login("EMAIL", "PW")
                    subject = "Housing Change in Huntington Beach"
                    text = "The housing plan in huntington beach has been updated. \n{}".format(url)
                    msg = 'Subject: {}\n\n{}'.format(subject, text)
                    server.sendmail("EMAIL", "EMAIL", msg)
                    server.quit()
                else:
                    logging.info('No change found.')
                    print('No Status Change')


if __name__ == '__main__':
    main()


schedule.every().day.at("12:00").do(main)

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute


