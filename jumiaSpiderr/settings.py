# -*- coding: utf-8 -*-

# Scrapy settings for jumiaSpiderr project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'jumiaSpiderr'

SPIDER_MODULES = ['jumiaSpiderr.spiders']
NEWSPIDER_MODULE = 'jumiaSpiderr.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Linux; rv:1.0) '

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
TELNETCONSOLE_ENABLED = False

# Enable mailing to uzezi okoro on completion of crawl process
STATSMAILER_RCPT = ['uzezio22@gmail.com']

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'jumiaSpiderr.middlewares.JumiaspiderrSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'jumiaSpiderr.middlewares.JumiaspiderrDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
EXTENSIONS = {
    'scrapy.extensions.telnet.TelnetConsole': None,
    'scrapy.extensions.statsmailer.StatsMailer': 500,
    'scrapy.extensions.memusage.MemoryUsage': 500,
    'scrapy.extensions.memdebug.MemoryDebugger': 500
}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'jumiaSpiderr.pipelines.JumiaspiderrPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


'''
########### Personal Settings ##########
'''
# Enable memory usage of spidee for profiling
MEMUSAGE_ENABLED = True
MEMUSAGE_WARNING_MB = 70
MEMDEBUG_ENABLE = True

# limit memory usage of spider
# MEMUSAGE_LIMIT_MB = 100

# Enable my custom extension


LOG_LEVEL = 'INFO'

DOWNLOAD_DELAY = .3
RANDOMIZE_DOWNLOAD_DELAY = True

USER_AGENT = 'Mozilla/5.0 (Linux; rv:1.0)'

ITEM_PIPELINES.update({
    'jumiaSpiderr.pipelines.PersFieldsPipelines': 300,
    'jumiaSpiderr.pipelines.PersDuplicatesPipeline': 350,
})

EXTENSIONS.update({
    'jumiaSpiderr.customextensions.'
})

'''
#################### Personal Settings ####################
'''
