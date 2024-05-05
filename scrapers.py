# imports
from bs4 import BeautifulSoup
from requests_html import HTMLSession


# scrapes the latest basketball headlines and converts them to an html-formatted string
def basketball():

    headlines = ""
    count = 0

    session = HTMLSession()
    page = session.get("https://www.nba.com")
    soup = BeautifulSoup(page.html.raw_html, "html.parser")
    for headline in soup.find_all("a", attrs={"data-id": "nba:home:headlines"}):
        if headline.text.strip() not in headlines and count < 20:
            headlines = headlines + "- " + headline.text.strip() + " <br> "
            count += 1

    return headlines


# scrapes the latest college basketball headlines and converts them to an html-formatted string
def cbasketball():

    headlines = ""
    count = 0

    session = HTMLSession()
    page = session.get("https://www.espn.com/mens-college-basketball/")
    soup = BeautifulSoup(page.html.raw_html, "html.parser")
    for headline in soup.find_all("a", attrs={"data-mptype": "headline"}):
        if headline.text.strip() not in headlines and count < 20:
            headlines = headlines + "- " + headline.text.strip() + " <br> "
            count += 1

    return headlines


# scrapes the latest college football headlines and converts them to an html-formatted string
def cfootball():

    count = 0
    headlines = ""

    session = HTMLSession()
    page = session.get("https://www.espn.com/college-football/")
    soup = BeautifulSoup(page.html.raw_html, "html.parser")
    for headline in soup.find_all("a", attrs={"data-mptype": "headline"}):
        if headline.text.strip() not in headlines and count < 20:
            headlines = headlines + "- " + headline.text.strip() + " <br> "
            count += 1

    return headlines


# scrapes the latest cricket headlines and converts them to an html-formatted string
def cricket():

    headlines = ""
    count = 0

    session = HTMLSession()
    page = session.get("https://www.espncricinfo.com/cricket-news")
    soup = BeautifulSoup(page.html.raw_html, "html.parser")
    for headline in soup.find_all("div", attrs={"class": "ds-flex ds-flex-col"}):
        title = headline.find("h2")
        if title.text.strip() not in headlines and count < 20:
            headlines = headlines + "- " + title.text.strip() + " <br> "
            count += 1

    return headlines


# scrapes the latest football headlines and converts them to an html-formatted string
def football():

    headlines = ""
    count = 0

    session = HTMLSession()
    page = session.get("https://www.nfl.com/")
    soup = BeautifulSoup(page.html.raw_html, "html.parser")
    for headline in soup.find_all(
        "span", attrs={"class": "nfl-o-headlinestack__item-text"}
    ):
        if headline.text.strip() not in headlines and count < 20:
            headlines = headlines + "- " + headline.text.strip() + " <br> "
            count += 1

    return headlines


# scrapes the latest soccer headlines and converts them to an html-formatted string
def soccer():

    headlines = ""
    count = 0

    session = HTMLSession()
    page = session.get("https://www.espn.com/soccer/")
    soup = BeautifulSoup(page.html.raw_html, "html.parser")
    for headline in soup.find_all("a", attrs={"data-mptype": "headline"}):
        if headline.text.strip() not in headlines and count < 20:
            headlines = headlines + "- " + headline.text.strip() + " <br> "
            count += 1

    return headlines
