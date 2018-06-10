import scrapy
import urllib.parse

from wikiproject.items import ImageItem

class PortraitSpider(scrapy.Spider):
    # spiderの名前
    name = 'portrait'
    # クロール対象とするドメインリスト
    allowed_domains = ['commons.wikimedia.org']
    # クロールを開始するurlのリスト. 1要素のタプルの末尾にはカンマが必要
    start_urls = ['https://commons.wikimedia.org/wiki/Category:17th-century_oil_portraits_of_standing_women_at_three-quarter_length',]


    def parse(self, response):
        """
        トップページに記載されているファイル名とリンクを取得
        """

        # wikipediaのホーム
        base_url = 'https://commons.wikimedia.org'

        for url in response.css('div.gallerytext a::attr("href")').extract():
            # 個別画像へのリンクがある場合は、parse_original_linkを呼ぶ
            yield scrapy.Request(response.urljoin(url), callback=self.parse_original_link)

        # 次ページリンクがあったらリンクをたどる
        next_page = response.css


    def parse_original_link(self, response):
        target_url = response.css('div.fullMedia a::attr("href")').extract_first()

        item = ImageItem()
        item["image_urls"] = []

        #yield {"target_url": target_url }
        item["image_urls"].append(target_url)

        return item
