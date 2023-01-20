<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
[![Fiverr][fiverr-shield]][fiverr-url]
[![Gmail][gmail-shield]][gmail-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/darideveloper/facebook-groups-post-bot">
    <img src="imgs/logo.gif" alt="Logo" width="200" height="160">
  </a>

<h3 align="center">Facebook Groups Post Bot</h3>

  <p align="center">
    Python bot for create text posts in facebook groups where you already are a member.
    <br />
    <a href="https://github.com/darideveloper/facebook-groups-post-bot/issues">Report Bug</a>
    ·
    <a href="https://github.com/darideveloper/facebook-groups-post-bot/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project have two scripts: __ save_groups.py __ and __ post_groups.py __.

The __ save_groups.py __ script is used to save the groups where you are a member in the data.json, searching them with specific keyword. This script is useful if you want to post in a lot of groups, because you can save the groups in the json file and use it in the __ post_groups.py __ script.

The __ post_groups.py __ script is used to post in spcific groups. In the data.json file you can save the groups where you want to post, and the script will post in all of them.

Warning: *This script is not for spamming groups, is for post in groups where you are a member, and you want to post in a lot of groups at the same time. I am not responsible for the use that you give to this script.*

### Built With


<div>
<a href="https://www.python.org/">
  <img src="https://cdn.svgporn.com/logos/python.svg" width="50" alt="python" title="python">
</a>
<a href="https://www.selenium.dev/">
  <img src="https://cdn.svgporn.com/logos/selenium.svg" width="50" alt="selenium" title="selenium">
</a>

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

* [Google chrome](https://www.google.com/intl/es-419/chrome/)
* [Python >=3.10](https://www.python.org/)
* [Git](https://git-scm.com/)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/darideveloper/facebook-groups-post-bot.git
   ```
2. Install python packages (opening a terminal in the project folder)
   ```sh
   python -m pip install -r requirements.txt 
   ```
3. Create a `.env` file and `data.json` file in the project folder.
4. Update your chrome path in the `.env` file (note: the chrome path is the folder where chrome data its installed)
   ```js
   CHROME_PATH = C:\Users\<<your-user-name>>\AppData\Local\Google\Chrome\User Data
   ```


<!-- USAGE EXAMPLES -->
## Usage

1. Before run the scripts, you need to login in your facebook account in chrome
2. (optional) Open the __ save_groups.py __ script with a code/text editor, and replace the "keyword" for search groups in the line 3
    ```python
    keyword = "python" # sample for search group where you are a member, about python
    ```
3. (optional) Run the __ save_groups.py __ script
    ```sh
    python save_groups.py
    ```
4. Open the "data.json" file, and add the groups where you want to post, and the text of the post in the "text" field
    ```json
    {
        "posts": [
            "This is a sample post 1",
            "This is a sample post 2",
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
5. Run the __ post_groups.py __ script
    ```sh
    python __post_groups__.py
    ```
6. Wait until the script finish, and enjoy your posts in the groups :)


<!-- ROADMAP -->
## Roadmap

- [x] Get all groups where you are a member related to a keyword
- [x] Create text post in groups
- [x] Select a random background color for each post

See the [open issues](https://github.com/darideveloper/facebook-groups-post-bot/issues) for a full list of proposed features (and known issues).


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Darideveloper - [@developerdari](https://twitter.com/developerdari) - darideveloper@gmail.com.com

Project Link: [https://github.com/darideveloper/facebook-groups-post-bot](https://github.com/darideveloper/facebook-groups-post-bot)


<!-- MARKDOWN LINKS & imgs -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/darideveloper/europeanstartups_scraper.svg?style=for-the-badge
[contributors-url]: https://github.com/darideveloper/facebook-groups-post-bot/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/darideveloper/europeanstartups_scraper.svg?style=for-the-badge
[forks-url]: https://github.com/darideveloper/facebook-groups-post-bot/network/members
[stars-shield]: https://img.shields.io/github/stars/darideveloper/europeanstartups_scraper.svg?style=for-the-badge
[stars-url]: https://github.com/darideveloper/facebook-groups-post-bot/stargazers
[issues-shield]: https://img.shields.io/github/issues/darideveloper/europeanstartups_scraper.svg?style=for-the-badge
[issues-url]: https://github.com/darideveloper/facebook-groups-post-bot/issues
[license-shield]: https://img.shields.io/github/license/darideveloper/europeanstartups_scraper.svg?style=for-the-badge
[license-url]: https://github.com/darideveloper/facebook-groups-post-bot/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/francisco-dari-hernandez-6456b6181/
[product-screenshot]: ./imgs/screenshot.gif
[gmail-url]: mailto:darideveloper@gmail.com
[fiverr-url]: https://www.fiverr.com/darideveloper
[gmail-shield]: https://img.shields.io/badge/-gmail-black.svg?style=for-the-badge&logo=gmail&colorB=555&logoColor=white
[fiverr-shield]: https://img.shields.io/badge/-fiverr-black.svg?style=for-the-badge&logo=fiverr&colorB=555&logoColor=white

<span>Last code update: <time datetime="2022-11-29" class="last-update">2023-01-20</time>
