import time, sys
from imapclient import IMAPClient

#
# YOU MAY NEED TO ENABLE IMAP IN YOUR EMAIL SETTINGS FOR THIS TO WORK
#

HOSTNAME = 'imap.gmail.com' # This is for gmail. If you use another email provider, please look in your IMAP settings
MAILBOX = 'Inbox'
EMAIL = 'myemail@gmail.com' # Put your email address here
PASSWORD = 'mysecurepassword' # Put your password here
NEWMAIL_OFFSET = 0 # If you have a bunch of unread emails you don't want to trigger, set this to how many you have, any more than this number will say you have an unread email

server = IMAPClient(HOSTNAME, use_uid=True, ssl=True)
server.login(EMAIL, PASSWORD)

unseen = server.folder_status(MAILBOX, ['UNSEEN'])
newmail_count = (unseen[b'UNSEEN'])
time.sleep(1.5)

if newmail_count > NEWMAIL_OFFSET:
    time.sleep(0.5)
    if newmail_count > 1:
        print("You have " + str(newmail_count) + " unread emails!")
    else:
        print("You have " + str(newmail_count) + " unread email!")
else:
    time.sleep(0.5)
    print("You have no unread emails!")

server.logout()
