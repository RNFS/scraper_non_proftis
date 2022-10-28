import scrapy
import utils

# import sqlite3
# con = sqlite3.connect("test.db")
# cur = con.cursor()
# cur.execute(     
#     "CREATE TABLE data( 
#         name, address, country, state, causes, website, mission, description, domain_scraped,
#          scraped_url, category, image 
#     )")

# print("open database OK")

class NonProfits(scrapy.Spider):
    name = "nonprofits"
    def start_requests(self):
        urls= [
            "https://www.pledge.to/organizations"
            # "https://www.pledge.to/organizations?cause=animals"
        ]
        
        for url in urls :
            yield scrapy.Request(url=url, callback=self.parse) 

    def parse(self, response):
        items = response.css("a.featured-fundraiser-link::attr(href)").getall()
        if len(items) >= 1:
            for item in items :
                yield response.follow(url=item, callback=self.parse_content)

        next_page = response.xpath("//a[@rel='next']/@href").get()
        if next_page:              
            next_page = 'https://www.pledge.to/' + next_page
            yield response.follow(url=next_page, callback=self.parse)
    
    def parse_content(self, response):
        country = response.xpath("//section[@class='mb-5']/ul[2]/li/a/text()").get()
        check_cou = list(utils.Validator.country(country))
        if check_cou[0]:
            name = response.xpath("//h1[@class='h3']/text()").get()
            causes = response.xpath("//section[@class='mb-5']/ul[1]/li/*/text()").getall()
            category = list(utils.Validator.category(causes))
            if len(category) == 0:
                category = "Unknown"
            else:
                category = "".join(category)                                 
            email = None
            phone = None
            reg_number = None
            reg_number_type = None
            reg_date = None
            gross_income = None
            address = response.xpath("//span[@class='h-adr adr']/*/text()").getall()
            address = " ".join(address)
            state = response.xpath("//abbr[@class='p-region region']/@title").get()
            causes = response.xpath("//section[@class='mb-5']/ul[1]/li/*/text()").getall()
            causes = "&".join(causes)
            website = response.xpath("//li[@class='px-1 px-sm-2']/a/@href").get()
            mission = response.xpath("//section[@class='mb-5']/p/text()").get()
            description = response.xpath("//section[@class='mb-5']/div/p/text()").get()
            image = response.xpath(f"//img[@alt='{name}']//@src").get()
            domain_scraped = "https://www.pledge.to/organizations"
            scraped_url = response.url 
            
            # conn.execute(
            #     "INSERT INTO data (name, address, country, state, causes, website, mission, description) \
            #     VALUES (name, address, country, state, causes, website, mission, description)")
            # # if country in self.countires:
            yield {
                "name":name,
                "address":address,
                "country":country,
                "state":state,
                "causes":causes,
                "website":website,
                "mission":mission,
                "description": description,
                "domain scraped": domain_scraped,
                "scraped url": scraped_url,
                "category":category,
                "image" : image 
            }
            

