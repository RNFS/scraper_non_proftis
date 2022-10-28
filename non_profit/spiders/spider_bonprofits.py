import scrapy
# import
import sqlite3

conn = sqlite3.connect('test.db')
print("open database OK")

class NonProfits(scrapy.Spider):
    name = "nonprofits"
    def start_requests(self):
        urls= [
            "https://www.pledge.to/organizations"
        ]
        
        for url in urls :
            yield scrapy.Request(url=url, callback=self.parse) 

    def parse(self, response):
        items = response.css("a.featured-fundraiser-link::attr(href)").getall()
        if len(items) >= 1:
            for item in items :
                yield response.follow(url=item, callback=self.parse_content)
       
        next_page = response.xpath("//a[@rel='next']/@href").get()
        print("#" * 50)
        print(next_page)
        print("#" * 50) 
        print("#" * 60) 
        print(f"{'https://www.pledge.to/'+ next_page}")
        print("#" * 50)
        if next_page:              
            next_page = 'https://www.pledge.to/' + next_page
            yield response.follow(url=next_page, callback=self.parse)
    
    def parse_content(self, response):
        name = response.xpath("//h1[@class='h3']/text()").get()
        address = response.xpath("//span[@class='h-adr adr']/*/text()").getall()
        address = " ".join(address)
        country = response.xpath("//section[@class='mb-5']/ul[2]/li/a/text()").get()
        state = response.xpath("//abbr[@class='p-region region']/@title").get()
        causes = response.xpath("//section[@class='mb-5']/ul[1]/li/*/text()").getall()
        causes = "&".join(causes)
        website = response.xpath("//li[@class='px-1 px-sm-2']/a/@href").get()
        mission = response.xpath("//section[@class='mb-5']/p/text()").get()
        description = response.xpath("//section[@class='mb-5']/div/p/text()").get()
        conn.execute(
            "INSERT INTO data (name, address, country, state, causes, website, mission, description) \
            VALUES (name, address, country, state, causes, website, mission, description)")
        # if country in self.countires:
        yield {
            "name":name,
            "address":address,
            "country":country,
            "state":state,
            "causes":causes,
            "website":website,
            "mission":mission,
            "description": description,

        }
        
