from scrapy import signals
from scrapy.exceptions import NotConfigured
from smtplib import SMTP_SSL
from email.message import EmailMessage
import sqlite3
import os
import json
import numpy as np
from concurrent.futures import ThreadPoolExecutor


class Mailer_Rct:
    """
        Scrapy extension to send message to recipients for their,
        desired category field or for all. To limit the amount of memeory used
        without excessive dampening of program speed. Numpy holds the data returned from
        the database for easy access.

        The Numpy portion of the code ensures that the database is only queried once and all the
        data is stored for quick access by the rest of the program during its run.
    """

    def __init__(self, recipients, sender, password):
        self.recipients = recipients
        self.sender = sender
        self.password = password

    @classmethod
    def from_crawler(cls, crawler):
        if not crawler.settings.getbool('MAILER_RCT_ENABLED'):
            raise NotConfigured

        # This will actually be gotten from a database, this is dummy data
        Requested_itmes = json.load('requested.json')

        recipients = crawler.settings.setdict('MAILER_RCT', Requested_itmes)
        mail = os.environ.get('USER')
        password = os.environ.get('PASSWORD')
        ext = cls(recipients, mail, password)

        crawler.signal.connect(ext.thread_send, signal=signals.spider_closed)

    def send_to_receiver(self, reciever, requested_category):
        msg = EmailMessage()

        msg['from'] = self.sender
        msg['to'] = reciever
        msg['subject'] = 'Best Picks from Jumia'

        with SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(self.sender, self.password)

            # sends a csv file, composed based on
            # msg.add_attachment()
            smtp.send_message(msg)

    def thread_send(self):
        with ThreadPoolExecutor(max_workers=4) as executor:
            executor.map(self.send_to_receiver,
                         self.recipients.keys(), self.recipients.values())
