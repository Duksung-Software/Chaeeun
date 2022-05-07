BOT_NAME = 'G_market2'

SPIDER_MODULES = ['G_market2.spiders']
NEWSPIDER_MODULE = 'G_market2.spiders'

ROBOTSTXT_OBEY = False

LOG_FILE = 'G_market2.log'

FEED_EXPORT_ENCODING='utf-8-sig'
FEED_EXPORT_FIELDS = ['Sort','Name','Price','URL']