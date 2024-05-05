# SportsNews

## Inspiration

I am a big sports fan. Although I am constantly checking social media, it is extremely chaotic and time-consuming to keep up with the latest headlines, and even harder to filter through what is important. I realized that although I rarely check websites such as nfl.com and nba.com for news, I always check my email, so I came up with a solution to my problem. I created a newsletter that would be sent to my inbox every morning with the most important sports news directly from the corresponding website and built this project. Basketball, college basketball, college football, cricket, football, and soccer are supported, and it is currently used by my dad and I.

## Data Processing Pipeline

1. In `scrapers.py`, the corresponding website is scraped (e.g. nfl.com for football) for the latest headlines/
2. In `template.py`, the headlines are formatted into HTML.
3. In `SportsNews.py`, formatted HMTL is sent as an email to the users on the sport's mailing list (stored in MongoDB).

The entire process is automated to occur at 9:00 am EST every morning through GitHub actions. 

## Scalability

This project is highly scalable. Follow these steps to add support for a new sport:
1. In `scrapers.py`, add a function to scrape the corresponding website for that sport.
2. In `template.py`, update the link accordingly for that sport.
3. In `SportsNews.py`, update the global variables accordingly for that sport.
