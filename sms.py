# SMS Central CLI script by Josh Burns <@prodigykit>
# Licensed under the BSD-3 License.

import profig
import requests
from datetime import datetime

# Globals
now = datetime.now().strftime("%H:%M:%S")
cfg = profig.Config('sms.cfg')

# Setup config
cfg.init('api.url', 'https://my.smscentral.com.au/api/v3.2')
cfg.init('api.username', None)
cfg.init('api.password', None)
cfg.init('message.campaign', "NEW MESSAGE: %s" % now)
cfg.init('message.prefix', None)
cfg.init('message.suffix', None)
cfg.sync()
# End Config

# Function that sends API request
def send_sms(recipient, message):
    msg = """
    %s
    
    %s
    
    %s
    """ % (cfg['message.prefix'], message, cfg['message.suffix'])
    payload = {
        "USERNAME": cfg['api.username'],
        "PASSWORD": cfg['api.username'],
        "ACTION": "send",
        "ORIGINATOR": "shared",
        "RECIPIENT": recipient,
        "CAMPAIGN": cfg['message.campaign'],
        "MESSAGE_TEXT": msg
    }
    r = requests.post(cfg['api.url'],
                      data=payload)
    return str(r.text)
