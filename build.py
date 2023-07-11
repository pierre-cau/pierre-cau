#!/usr/bin/env python3
from profile_readme import get_github_context, ProfileGenerator
import feedparser
import requests
import pandas as pd
import time as t

def get_weather(city):
    # declare the client. format defaults to the metric system (celcius, km/h, etc.)
    url = 'https://wttr.in/{}?m&format=3'.format(city)
    res = requests.get(url)
    return res.text

def get_feed(feed_url):
    feed = feedparser.parse(feed_url)
    entries = feed.entries
    from operator import itemgetter
    feed_sorted = sorted(entries, key=itemgetter('published_parsed'), reverse=True)

    return feed_sorted[0:4]


if __name__ == "__main__":
    weather = get_weather("Lyon")
    date = t.strftime("%d/%m/%Y")
    context = {
        "weather" : weather,
        "linkedin": {
            "url": "https://www.linkedin.com/in/pierre-cau/",
            "badge": "![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)",
        },
        "twitter": {
            "url": "https://twitter.com/CauPierre22",
            "badge": "![Twitter](https://img.shields.io/badge/twitter-%231DA1F2.svg?style=for-the-badge&logo=twitter&logoColor=white)",
        },
        "facebook": {
            "url": "https://www.facebook.com/Pcau22410/",
            "badge": "![Facebook](https://img.shields.io/badge/facebook-%231877F2.svg?style=for-the-badge&logo=facebook&logoColor=white)",
        },
        "badges": [
            "![Python](https://img.shields.io/badge/python-75bba4?style=for-the-badge&logo=python&logoColor=ecf22d)",
            "![Shell Script](https://img.shields.io/badge/shell_script-%23121011.svg?style=for-the-badge&logo=gnu-bash&logoColor=white)",
            "![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)",
            "![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white)",
            "![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)",
            "![Apache](https://img.shields.io/badge/apache-%23D42029.svg?style=for-the-badge&logo=apache&logoColor=white)",
            "![Google Cloud](https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white)",
            "![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)",
            "![GitLab](https://img.shields.io/badge/gitlab-%23F05033?style=for-the-badge&logo=gitlab&logoColor=white)",
            "![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)",
            "![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)",
            "![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)",
            "![R](https://img.shields.io/badge/R-blue?style=for-the-badge&logo=R&logoColor=white&link=https%3A%2F%2Fabout.gitlab.com%2F)",
            "![RStudio](https://img.shields.io/badge/RStudio-blue?style=for-the-badge&logo=RStudio&logoColor=white&link=https%3A%2F%2Fabout.gitlab.com%2F)",
            "![Jupyter](https://img.shields.io/badge/Jupyter-F37626.svg?style=for-the-badge&logo=Jupyter&logoColor=white)",
            "![Anaconda](https://img.shields.io/badge/Anaconda-44A833?style=for-the-badge&logo=Anaconda&logoColor=white)",
            "![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=Docker&logoColor=white)",
            "![AndroidStudio](https://img.shields.io/badge/AndroidStudio-3DDC84?style=for-the-badge&logo=AndroidStudio&logoColor=white)",
            "![Arduino](https://img.shields.io/badge/Arduino-00979D?style=for-the-badge&logo=Arduino&logoColor=white)",
            "![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=Java&logoColor=white)",
            "![Kotlin](https://img.shields.io/badge/Kotlin-F37626?style=for-the-badge&logo=Kotlin&logoColor=white)",
            "![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=JavaScript&logoColor=black)",
            "![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=HTML5&logoColor=white)",
            "![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=CSS3&logoColor=white)",
            "![Flutter](https://img.shields.io/badge/Flutter-02569B?style=for-the-badge&logo=Flutter&logoColor=white)",
        ],
        "mykofi": {
            "url": "https://ko-fi.com/pierre_cau",
            "badge": "![Ko-Fi](https://img.shields.io/badge/Ko--fi-F16061?style=for-the-badge&logo=ko-fi&logoColor=white)"
        },
        "links": [],
           # FORMAT : 
                #"title": "Vagrant",
                #"link": "https://blog.stephane-robert.info/tags/vagrant/"
        "date": date,
        "quote": "“The true wisdom is in knowing you know nothing.” - Socrates",
    }

    context.update(**get_github_context("pierre-cau"))
    #print(context)

    ProfileGenerator.render(
        template_path="README-TEMPLATE.j2",
        output_path="README.md",
        context=context,
    )
