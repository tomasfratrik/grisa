# Google Reverse Image Search API
## Brief
This api scrapes google reverse image search results using `selenium` bot and `beautifulsoup4` for scraping.

## Installation
Import to project folder inside your project folder
```python
from grisa import Grisa
```

### Requirements 
Within your wirtual enviroment install requirements with `pip install -r requirements.txt`

### Return format (JSON)
- returns tuple of 2 values
- first value are similar images, which is a list of objects:
``` 
{
    'website': website name,
    'description': description,
    'imageurl': url link to image,
    'link': url link to ad listing,
    'position': position in which it was found,
}
```
Careful, the description is incomplete, containing sometimes only 5 words!

- second are source images, which are same as similar with addition of:
```
'resolution': (x,y),
```


## API
### Check `Usage example` section for usage example
Grisa class has following methods:
- `options_add_argument("option")` - Add argument to options
- `set_driver_path(DRIVER_PATH)`- Set path to chromedriver
- `init_binary(BINARY)` - Set binary path
- `init_driver()` - Init driver
- `run(ABSOLUTE_PATH_TO_IMAGE, accept_cookies=True/False, local_dev=True/False)` - Run bot
    - accept_cookies (default: True) -> If you are not logged in to google account, 
                                        (in selenium browser, which you probably aren't), you need to accept cookies-
        - True: Accept cookies
        - False: Do not accept cookies
    - local_dev (default: True) -> Different way to click on elements on page using selenium 
        - True: was used when running on local machine
        - False: was used when deployed to heroku, otherwise wasn't working 
- `get_page_source()` - Get page source
- `scrape_similiar(page_source)` - Scrape similiar images
- `go_to_source()` - Go to source image
- `scrape_source(page_source)` - Scrape source image
- `driver_quit()` - Quit driver



## Usage example:
```python
import os
from grisa import Grisa
 
grisa = Grisa()
grisa.options_add_argument('--headless')
grisa.options_add_argument('--no-sandbox')
grisa.options_add_argument('--disable-dev-shm-usage')
grisa.options_add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
grisa.set_driver_path(PATH_TO_YOU_CHROMEDRIVER)
grisa.init_driver()
grisa.run(ABSOLUTE_PATH_TO_IMAGE, accept_cookies=True, local_dev=True)
page_source = grisa.get_page_source()
similiar_img_json = grisa.scrape_similiar(page_source)
grisa.go_to_source()
page_source = grisa.get_page_source()
source_img_json = grisa.scrape_source(page_source)
grisa.driver_quit()
```

