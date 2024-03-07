from bs4 import BeautifulSoup
from .identificators import SimiliarImgPage, SourceImgPage
import re

class Scraper:

    @staticmethod
    def scrape(page_src, id):
        soup = BeautifulSoup(page_src, 'html.parser')
        # container on website with possible ads
        container = soup.find_all(id.CONTAINER_TAG.value, class_=id.CONTAINER.value)
        for item in container:
            website = item.find_all(id.WEBSITE_TAG.value, class_=id.WEBSITE.value)
            desc = item.find_all(id.DESC_TAG.value, class_=id.DESC.value)
            imgURL = item.find_all(id.IMGURL_TAG.value, class_=id.IMGURL.value)
            link = item.find_all(id.LINK_TAG.value, class_=id.LINK.value)
            if id == SourceImgPage:
                resolution = item.find_all(id.RESOLUTION_TAG.value, class_=id.RESOLUTION.value)
        data = []

        pos = 0
        for i in range(len(website)):
            try:
                new_data = {
                    'website': website[i].text,
                    'description': desc[i].text,
                    'imageurl': imgURL[i][id.IMGURL_SRC.value],
                    'link': link[i]['href'],
                    "position": pos
                }

                if id == SourceImgPage:
                    input_string = resolution[i].text
                    match = re.search(r'(\d+)x(\d+)', input_string)

                    if match:
                        resolution_tuple = (int(match.group(1)), int(match.group(2)))
                        new_data['resolution'] = resolution_tuple
                    else:
                        new_data['resolution'] = None
                else:
                    new_data['resolution'] = None
                pos += 1
                data.append(new_data)
            except Exception as err:
                pass

        return data

    @staticmethod
    def scrape_similiar(page_src):
        data = Scraper.scrape(page_src, SimiliarImgPage)
        return data
    
    @staticmethod
    def scrape_source(page_src):
        data = Scraper.scrape(page_src, SourceImgPage)
        return data
