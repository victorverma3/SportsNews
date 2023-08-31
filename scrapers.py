#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 10:45:43 2023

@author: victor
"""

# Imports
from bs4 import BeautifulSoup
import json
import requests as requests


# Scrapers
def basketball():
    """This function scrapes the latest headlines from nba.com and returns
    them as a string formatted in html."""
    headlines = ""
    page = requests.get("https://www.nba.com")
    soup = BeautifulSoup(page.text, "html.parser")
    for headline in soup.find_all("a", attrs={"data-id": "nba:home:headlines"}):
        if headline.text.strip() not in headlines:
            headlines = headlines + "- " + headline.text.strip() + " <br> "
    return headlines


def cbasketball():
    """This function scrapes the latest headliens from espn.com/mens-college-basketball
    and returns them as a string formatted in html."""
    headlines = ""
    page = requests.get("https://www.espn.com/mens-college-basketball/")
    soup = BeautifulSoup(page.text, "html.parser")
    for headline in soup.find_all("a", attrs={"data-mptype": "headline"}):
        if headline.text.strip() not in headlines:
            headlines = headlines + "- " + headline.text.strip() + " <br> "
    return headlines


def cfootball():
    """This function scrapes the latest headliens from espn.com/college-football
    and returns them as a string formatted in html."""
    headlines = ""
    page = requests.get(
        "http://site.api.espn.com/apis/site/v2/sports/football/college-football/news"
    )
    data = json.loads(page.text)
    for article in data["articles"]:
        if article["headline"] not in headlines:
            headlines = headlines + "- " + article["headline"] + " <br> "
    return headlines


def cricket():
    """This function scrapes the latest headlines from espncricinfo.com/cricket-news
    and returns them as a string formatted in html."""
    headlines = ""
    page = requests.get("https://www.espncricinfo.com/cricket-news")
    soup = BeautifulSoup(page.text, "html.parser")
    for headline in soup.find_all("div", attrs={"class": "ds-flex ds-flex-col"}):
        title = headline.find("h2")
        if title.text.strip() not in headlines:
            headlines = headlines + "- " + title.text.strip() + " <br> "
    return headlines


def football():
    """This function scrapes the latest headlines from nfl.com and returns
    them as a string formatted in html."""
    headlines = ""
    page = requests.get("https://www.nfl.com/")
    soup = BeautifulSoup(page.text, "html.parser")
    for headline in soup.find_all(
        "span", attrs={"class": "nfl-o-headlinestack__item-text"}
    ):
        if headline.text.strip() not in headlines:
            headlines = headlines + "- " + headline.text.strip() + " <br> "
    return headlines


def soccer():
    """This function scrapes the latest headlines from espn.com/soccer
    and returns them as a string formatted in html."""
    headlines = ""
    page = requests.get("https://www.espn.com/soccer")
    soup = BeautifulSoup(page.text, "html.parser")
    for headline in soup.find_all("a", attrs={"data-mptype": "headline"}):
        if headline.text.strip() not in headlines:
            headlines = headlines + "- " + headline.text.strip() + " <br> "
    return headlines
