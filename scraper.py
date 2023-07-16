import os
import json
import random
from dotenv import load_dotenv
from logs import logger
from time import sleep
from scraping_manager.automate import WebScraping

# Read env vars 
load_dotenv ()
CHROME_FOLDER = os.getenv ("CHROME_FOLDER")
WAIT_MIN = int(os.getenv ("WAIT_MIN"))

class Scraper (WebScraping):
    
    def __init__ (self):
        """ read data from json file and start scraper using chrome folder """
        
        # Files paths
        current_folder = os.path.dirname(__file__)
        self.data_path = os.path.join (current_folder, "data.json")

        # Read json data
        with open (self.data_path, encoding="UTF-8") as file:
            self.json_data = json.loads (file.read())

        # Start scraper
        super().__init__(chrome_folder=CHROME_FOLDER, start_killing=True)
        
    def post_in_groups (self):
        """ Publish each post in each group fromd ata file """

        # Css selectors
        selectors = {
            "display_input": ".x6s0dn4.x78zum5.x1l90r2v.x1pi30zi.x1swvt13.xz9dl7a > span.x1emribx + div.x1i10hfl",
            "input": 'div.notranslate._5rpu[role="textbox"]',
            "display_themes": 'div[aria-label="Show Background Options"]',
            "theme": 'div.x1qjc9v5.x78zum5.x1q0g3np.xozqiw3.xcud41i.x139jcc6.x1n2onr6.xl56j7k > div:nth-child(index) > div[aria-pressed="false"]',
            "show_image_input": '[aria-label="Photo/video"]',
            "add_image": 'input[type="file"][accept^="image/*"]',
            "submit": '[aria-label="Post"][role="button"]',
        }

        # Loop each group
        posts_done = []
        for group in self.json_data["groups"]:
            self.set_page(group)
            sleep (5)
            self.refresh_selenium()
            
            for post in self.json_data["posts"]:
                
                post_text = post["text"]
                post_image = post["image"]
                
                # Open text input
                self.click_js (selectors["display_input"])
                self.refresh_selenium()
                
                # Write text
                try:
                    self.send_data(selectors["input"], post_text)
                except:
                    logger.error('Error writing text: "{post}" ({group})')
                    continue
                
                # Add image or theme
                if post_image:
                    # Upload image
                    self.click_js(selectors["show_image_input"])
                    self.refresh_selenium()
                    self.send_data(selectors["add_image"], post_image)
                else:
                    
                    try:
                        self.refresh_selenium()
                        self.click_js(selectors["display_themes"])
                    except:
                        logger.error(f"Error showing themes. Theme skipped: '{post}' ({group})")
                    else:
                        # Select theme
                        random_theme_index = str(random.randrange(2, 10))
                        random_theme = selectors["theme"].replace("index", random_theme_index)
                        self.refresh_selenium()
                        self.click_js(random_theme)
                
                # submit
                self.refresh_selenium()
                self.click_js(selectors["submit"])
                sleep (WAIT_MIN*60)
                
                # Save register of post
                posts_done.append ([group, post])
                
                # Logs
                logger.info (f'post done: "{post}" ({group})')
                
    def save_groups (self, keyword):
        """ Sedarch already signed groups and save them in data file """
        
        # Set groups page
        logger.info ("Searching groups...")
        search_page = f"https://www.facebook.com/groups/search/groups/?q={keyword}"
        self.set_page(search_page)
        sleep (3)
        self.refresh_selenium()
        
        links_num = 0
        tries_count = 0
        
        selectors = {
            "group_link": '.x1yztbdb div[role="article"] a[aria-label="Visit"]',
        }
        
        # Scroll for show already logged groups
        while True:
            self.go_bottom()
            new_links_num = len(self.get_elems (selectors["group_link"]))
            if new_links_num == links_num:
                tries_count += 1
            else: 
                links_num = new_links_num
                self.refresh_selenium()
                
            if tries_count == 3:
                break
            
        # Get all link of the groups
        links = self.get_attribs (selectors["group_link"], "href")
        logger.info (f"{len(links)} groups found and saved")
        
        # Save links in jdon file
        if links:
            self.json_data["groups"] = links
            with open (self.data_path, "w", encoding="UTF-8") as file:
                file.write (json.dumps(self.json_data))
                
            
        
         
