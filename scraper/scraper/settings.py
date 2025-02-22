import os

from .items import (
    CityCouncilAgendaItem,
    CityHallBidItem,
    CityHallContractItem,
    CityHallPaymentsItem,
    GazetteEventItem,
    LegacyGazetteItem,
)

# general
BOT_NAME = "maria-quiteria"
SPIDER_MODULES = ["scraper.spiders"]
NEWSPIDER_MODULE = "scraper.spiders"
ROBOTSTXT_OBEY = True
COOKIES_ENABLED = False
EXTENSIONS = {
    "scraper.extensions.SentryLogging": -1,
    "spidermon.contrib.scrapy.extensions.Spidermon": 500,
}
SENTRY_DSN = os.getenv("SENTRY_DSN", "")

# pipelines
ITEM_PIPELINES = {
    "scraper.pipelines.ExtractFileContentPipeline": 100,
    "spidermon.contrib.scrapy.pipelines.ItemValidationPipeline": 200,
}
FILES_STORE = f"{os.getcwd()}/data/"
KEEP_FILES = os.getenv("KEEP_FILES", False)

# http cache
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 86400  # 24 hours

# testing
SPIDERMON_ENABLED = True
SPIDERMON_VALIDATION_ADD_ERRORS_TO_ITEMS = True
SPIDERMON_VALIDATION_MODELS = {
    LegacyGazetteItem: "scraper.validators.LegacyGazetteItem",
    GazetteEventItem: "scraper.validators.GazetteEventItem",
    CityCouncilAgendaItem: "scraper.validators.CityCouncilAgendaItem",
    CityHallContractItem: "scraper.validators.CityHallContractItem",
    CityHallBidItem: "scraper.validators.CityHallBidItem",
    CityHallPaymentsItem: "scraper.validators.CityHallPaymentsItem",
}

# monitoring
SPIDERMON_SPIDER_CLOSE_MONITORS = ("scraper.monitors.SpiderCloseMonitorSuite",)

# bot
SPIDERMON_TELEGRAM_SENDER_TOKEN = os.getenv("SPIDERMON_TELEGRAM_SENDER_TOKEN", None)
SPIDERMON_TELEGRAM_RECIPIENTS = [os.getenv("SPIDERMON_TELEGRAM_CHANNEL", None)]
