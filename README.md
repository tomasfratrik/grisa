# Google reverse image search API
## Brief
This api is used to scrape google reverse image search results using selenium bot and beautifulsoup4 for scraping.

## Installation:
This is script is ment to be used as a module. To install it, run:
git submodule add <link to this repo>
then import to your project using:
from grisa import Grisa, SimiliarImgPage, SourceImgPage


## Usage example:
* PATH="path to your chromedriver"
* grisa = Grisa()
* grisa.set_driver_path(PATH)
- possible to set binary path here
* grisa.init_driver()
* grisa.run(absolute path to image)
* page_source = grisa.get_page_source()
* similiar_img_json = grisa.scrape_similiar(page_source)
* grisa.driver_quit()

## Todos:
- [x] Add support for scraping source image page
- [x] Support for images as url links

