from libs.scraper import Scraper


def main():
    
    while True:
        
        scraper = Scraper()
        option = input("1) Save groups\n2) Post in groups\n3) Exit\nOption: ")
        if option == "1":
            keyword = input("Enter keyword: ")
            scraper.save_groups(keyword)
        elif option == "2":
            scraper.post_in_groups()
        elif option == "3":
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()