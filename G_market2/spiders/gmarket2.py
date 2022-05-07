import scrapy
from G_market2.items import GMarket2Item

keyword = input('원하는 키워드를 입력해주세요 : ').split(' ')


while True:
    sort = input('원하는 정렬을 선택하세요. 판매인기순(8), 낮은 가격순(1), 높은 가격순(2), 상품평 많은 순(13), 신규 상품순(3) : ')

    if sort == '8' or sort == '1' or sort == '2' or sort == '13' or sort == '3':
        break

if sort == '8':
    Sort='판매인기순'
if sort == '1':
    Sort='낮은 가격순'
if sort == '2':
    Sort='높은 가격순'
if sort == '13':
    Sort='상품명 많은 순'
if sort == '3':
    Sort='신규 상품 순'

key_word = '+'.join(keyword)

#무료배송이고 입력 받은 keyword url --> https://browse.gmarket.co.kr/search?keyword=야구&s=8
URL = 'https://browse.gmarket.co.kr/search?keyword='+ key_word +'&f=d:f&s='+ sort

class Gmarket2Spider(scrapy.Spider):
    name = 'gmarket2'

    #크롤링 진행 url
    start_urls = [URL]

    def parse(self, response):
        
        global url

        #세부상품 URL 추출
        for i in range(1,101):
            URL = response.xpath(f'//*[@id="section__inner-content-body-container"]/div[2]/div[{i}]/div/div[2]/div[1]/div[1]/span/a')
            div = response.xpath(f'//*[@id="section__inner-content-body-container"]/div[2]/div[{i}]')

            #URL이 빈칸이 아니라면 span 앞이 div[1]이다
            if (URL != []):
                href = div.xpath('./div[1]/div[2]/div[1]/div[1]/span/a/@href')
                url = response.urljoin(href[0].extract())
                yield scrapy.Request(url, callback = self.parse_page_content1)

            #URL이 빈칸이라면 span 앞이 div[2]이다.
            if (URL == []):
                href = div.xpath('./div[1]/div[2]/div[1]/div[2]/span/a/@href')
                url = response.urljoin(href[0].extract())
                yield scrapy.Request(url, callback = self.parse_page_content2) #url 세부항목으로 들어가기 위한 상황

    def parse_page_content1(self,response):

        item = GMarket2Item()

        item['Sort']= Sort
        item['Name']=response.xpath('//*[@id="itemcase_basic"]/div/h1/text()')[0].extract()
        item['Price']=response.xpath('//*[@id="itemcase_basic"]/div/p/span/strong/text()')[0].extract()
        item['URL']=url

        return item

    def parse_page_content2(self,response):

        item = GMarket2Item()

        item['Sort']= Sort
        item['Name']=response.xpath('//*[@id="itemcase_basic"]/div/h1/text()')[0].extract()
        item['Price']=response.xpath('//*[@id="itemcase_basic"]/div/p/span/strong/text()')[0].extract()
        item['URL']=url

        return item