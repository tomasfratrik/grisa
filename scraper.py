from bs4 import BeautifulSoup
from .identificators import SimiliarImgPage, SourceImgPage

class Scraper:
    def scrape_similiar(page_src):
        soup = BeautifulSoup(page_src, 'html.parser')
        # container on website with possible ads
        container = soup.find_all(SimiliarImgPage.CONTAINER_TAG.value, class_=SimiliarImgPage.CONTAINER.value)
        for item in container:
            website = item.find_all(SimiliarImgPage.WEBSITE_TAG.value, class_=SimiliarImgPage.WEBSITE.value)
            desc = item.find_all(SimiliarImgPage.DESC_TAG.value, class_=SimiliarImgPage.DESC.value)
            imgURL = item.find_all(SimiliarImgPage.IMGURL_TAG.value, class_=SimiliarImgPage.IMGURL.value)
            link = item.find_all(SimiliarImgPage.LINK_TAG.value, class_=SimiliarImgPage.LINK.value)
        data = []
        SKIP_SAME_LINKS_LEN = 60
        if(id == SimiliarImgPage):
            SKIP_SAME_LINKS_LEN = 0
        num = 0
        for i in range(len(website)):
            try:
                new_data = {
                    'website': website[i].text,
                    'description': desc[i].text,
                    'imageURL': imgURL[i][SimiliarImgPage.IMGURL_SRC.value],
                    # 'imageURL': imgURL[i].text,
                    'link': link[i + SKIP_SAME_LINKS_LEN]['href'],
                    "position": num
                }
                num += 1
                data.append(new_data)
            except:
                print(f"error at {i}")
                pass

        return data
    # def scrape_source(page_src):
    #     soup = BeautifulSoup(page_src, 'html.parser')

    #     # container on website with possible ads
    #     container = soup.find_all(SimiliarImgPage.CONTAINER_TAG.value, class_=SimiliarImgPage.CONTAINER.value)
    #     for item in container:
    #         website = item.find_all(SimiliarImgPage.WEBSITE_TAG.value, class_=SimiliarImgPage.WEBSITE.value)
    #         desc = item.find_all(SimiliarImgPage.DESC_TAG.value, class_=SimiliarImgPage.DESC.value)
    #         imgURL = item.find_all(SimiliarImgPage.IMGURL_TAG.value, class_=SimiliarImgPage.IMGURL.value)
    #         link = item.find_all(SimiliarImgPage.LINK_TAG.value, class_=SimiliarImgPage.LINK.value)

    #     data = []
    #     SKIP_SAME_LINKS_LEN = 60
    #     if(id == SimiliarImgPage):
    #         SKIP_SAME_LINKS_LEN = 0
    #     num = 0
    #     for i in range(len(website)):
    #         try:
    #             new_data = {
    #                 'website': website[i].text,
    #                 'description': desc[i].text,
    #                 'imageURL': imgURL[i][SimiliarImgPage.IMGURL_SRC.value],
    #                 # 'imageURL': imgURL[i].text,
    #                 'link': link[i + SKIP_SAME_LINKS_LEN]['href'],
    #                 "position": num
    #             }
    #             num += 1
    #             data.append(new_data)
    #         except:
    #             print(f"error at {i}")
    #             pass

    #     return data
