# SMS Central CLI script by Josh Burns <@prodigykit>
# Licensed under the BSD-3 License.

import profig
from datetime import datetime.
now = datetime.now().strftime("%H:%M:%S")

# Setup config
cfg = profig.Config('sms.cfg')
cfg.init('api.url', 'https://my.smscentral.com.au/api/v3.2')
cfg.init('api.username', None)
cfg.init('api.password', None)
cfg.init('message.campaign', "NEW MESSAGE: %s" % now)
cfg.init('message.prefix', None)
cfg.init('message.suffix', None)
cfg.sync()
# End Config
