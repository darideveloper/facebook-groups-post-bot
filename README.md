<div><a href='https://github.com/darideveloper/facebook-groups-post-bot/blob/master/LICENSE' target='_blank'>
                <img src='https://img.shields.io/github/license/darideveloper/facebook-groups-post-bot.svg?style=for-the-badge' alt='MIT License' height='30px'/>
            </a><a href='https://www.linkedin.com/in/francisco-dari-hernandez-6456b6181/' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=LinkedIn&color=0A66C2&logo=LinkedIn&logoColor=FFFFFF&label=' alt='Linkedin' height='30px'/>
            </a><a href='https://t.me/darideveloper' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Telegram&color=26A5E4&logo=Telegram&logoColor=FFFFFF&label=' alt='Telegram' height='30px'/>
            </a><a href='https://github.com/darideveloper' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=GitHub&color=181717&logo=GitHub&logoColor=FFFFFF&label=' alt='Github' height='30px'/>
            </a><a href='https://www.fiverr.com/darideveloper' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Fiverr&color=222222&logo=Fiverr&logoColor=1DBF73&label=' alt='Fiverr' height='30px'/>
            </a><a href='https://discord.com/users/992019836811083826' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Discord&color=5865F2&logo=Discord&logoColor=FFFFFF&label=' alt='Discord' height='30px'/>
            </a><a href='mailto:darideveloper@gmail.com?subject=Hello Dari Developer' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Gmail&color=EA4335&logo=Gmail&logoColor=FFFFFF&label=' alt='Gmail' height='30px'/>
            </a><a href='https://www.twitch.tv/darideveloper' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Twitch&color=b9a3e3&logo=Twitch&logoColor=ffffff&label=' alt='Twitch' height='30px'/>
            </a></div><div align='center'><br><br><img src='https://github.com/darideveloper/facebook-groups-post-bot/raw/master/imgs/logo.gif' alt='Facebook Groups Post Bot' height='80px'/>

# Facebook Groups Post Bot

Python bot for create text posts in facebook groups where you already are a member.
Project type: **personal**

</div><br><details>
            <summary>Table of Contents</summary>
            <ol>
<li><a href='#buildwith'>Build With</a></li>
<li><a href='#media'>Media</a></li>
<li><a href='#details'>Details</a></li>
<li><a href='#install'>Install</a></li>
<li><a href='#settings'>Settings</a></li>
<li><a href='#run'>Run</a></li>
<li><a href='#roadmap'>Roadmap</a></li></ol>
        </details><br>

# Build with

<div align='center'><a href='https://www.python.org/' target='_blank'> <img src='https://cdn.svgporn.com/logos/python.svg' alt='Python' title='Python' height='50px'/> </a><a href='https://www.selenium.dev/' target='_blank'> <img src='https://cdn.svgporn.com/logos/selenium.svg' alt='Selenium' title='Selenium' height='50px'/> </a></div>

# Details

This project have two scripts **save_groups**.py **post_groups**.py

The **save_groups**.py script is used to save the groups where you are a member in the data.json, searching them with specific keyword. This script is useful if you want to post in a lot of groups, because you can save the groups in the json file and use it in the **post_groups**.py script.


The **post_groups**.py script is used to post in spcific groups. In the data.json file you can save the groups where you want to post, and the script will post in all of them (a random post each time)

Warning: This script is not for spamming groups, is for post in groups where you are a member, and you want to post in a lot of groups at the same time. I am not responsible for the use that you give to this script.

# Install

## Prerequisites

* [Google chrome](https://www.google.com/intl/es-419/chrome/)
* [Python >=3.10](https://www.python.org/)
* [Git](https://git-scm.com/)

## Installation

1. Clone the repo

   ```sh
   git clone https://github.com/darideveloper/facebook-groups-post-bot.git
   ```

2. Install python packages (opening a terminal in the project folder)

   ```sh
   python -m pip install -r requirements.txt 
   ```

3. Create a `.env` file and `data.json` file in the project folder.

# Settings

Update your chrome path in the `.env` file (note: the chrome path is the folder where chrome data its installed)

```js
CHROME_PATH = C:Users<<your-user-name>>AppDataLocalGoogleChromeUser Data
```

# Run

1. Before run the scripts, you need to login in your facebook account in chrome

2. (optional) Open the **save_groups**.py script with a code/text editor, and replace the "keyword" for search groups in the line 3

    ```python
    keyword = "python" # sample for search group where you are a member, about python
    ```

3. (optional) Run the **save_groups**.py script

    ```sh
    python __save_groups__.py
    ```

4. Open the "data.json" file, and add the groups where you want to post, and the text of the post in the "text" field

    ```json
        {
        "posts": [
            {
                "text": "text post 1",
                "image": "{image path}"
            },
            {
                "text": "text post 2",
                "image": "{image path}"
            },
            {
                "text": "text post 3",
                "image": ""
            },
        ],
        "groups": [
            "https://www.facebook.com/groups/sample-group-1/",
            "https://www.facebook.com/groups/sample-group-2/",
            "https://www.facebook.com/groups/sample-group-3/",
            "https://www.facebook.com/groups/sample-group-4/",
            "https://www.facebook.com/groups/sample-group-5/",
            "https://www.facebook.com/groups/sample-group-6/",
            "https://www.facebook.com/groups/sample-group-7/",
            "https://www.facebook.com/groups/sample-group-8/"
        ]
    }
    ```

5. Run the **post_groups**.py script

    ```sh
    python __post_groups__.py
    ```

6. Wait until the script finish, and enjoy your posts in the groups :

# Roadmap

- [x] Get all groups where you are a member related to a keyword
- [X] Single post per group
- [X] Choose a random post each time
- [X] Optional image in posts