# Google reverse image search API
## Brief
This api is able to scrape google reverse image search results using selenium bot and beautifulsoup4 for scraping.

## Installation
Import to project folder inside your project folder
```python
from grisa import Grisa
```

## Requirements
- Python 3.6+
- Selenium
- Beautifulsoup4
- ChromeDriver

## Usage example:
```python
PATH="path to your chromedriver"
grisa = Grisa()
grisa.set_driver_path(PATH)
# possible to set binary
# grisa.init_binary("GOOGLE_CHROME_BIN")
grisa.init_driver()
grisa.run(absolute path to image)
page_source = grisa.get_page_source()
similiar_img_json = grisa.scrape_similiar(page_source)
grisa.go_to_source()
page_source = grisa.get_page_source()
source_img_json = grisa.scrape_source(page_source)
grisa.driver_quit()
```

## Todos:
- [x] Support for images as url links

