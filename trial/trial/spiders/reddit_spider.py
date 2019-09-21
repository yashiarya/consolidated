import scrapy
from ..items import TrialItem


class redditScrapy(scrapy.Spider):
    name = 'reddit'
    start_urls = [
        'https://www.propertycloud.mu/houses-for-sale?sortby=pricedesc'
    ]

    def parse(self, response):

        storeditem = TrialItem()

        all_containers = response.css('div.cleafix')

        for item in all_containers:
            title = item.css('.teaser::text').extract()
            area = item.css('.area-attribute::text').extract()
            address = item.css('.full-address::text').extract()
            listing = item.css('.listing-heading::text').extract()
            details = item.css('.truncate::text').extract()

            storeditem['title'] = title
            storeditem['area'] = area
            storeditem['address'] = address
            storeditem['listing'] = listing
            storeditem['details'] = details

            yield storeditem
