# SportsNews

# Inspiration

I am a big sports fan, especially of football and basketball. Although I am constantly checking social media, it is extremely chaotic and time consuming to keep up with all of the latest headlines, and even harder to filter through what is actually important. It came to my realization that although I rarely check websites such as nfl.com and nba.com for news, I always check my email, and so I came up with a solution to my problem. I decided that I would create a newsletter that would be sent to my inbox every morning with the most important football and basketball news, and built this project.

# Methodology

The first step in building this project was obtaining the required information. In the file scrapers.py, I created two functions to scrape the nfl.com and nba.com websites for their latest headlines. After gathering this data, I next created sportsnews.py, which is the main file in the project. In this file, I established a connection to a hotmail account server in order to allow the script to send emails directly from my desired account. I created an email alias and the script reads the password from my .env file. At this point I had two scripts which could gather sports headlines and send emails.

Next I decided that the email should also be in a format that is pleasing to the eye of any readers. To do this I created a new file, templates.py, in which I formatted the email using HTML/CSS. I also added HTML tags into the return strings of the scraper functions that I created earlier in order to seamlessly transition the data into the HTML template. I then used a python package to attach the HTML text into the email. I added the variables footballList basketballList in my .env file to store their respective mailing lists as comma-delimited strings of emails. This allows the program to automatically send a formatted email containing the latest football and basketball headlines to everyone on the mailing list.

# Scalability

This project is highly scalable. In scrapers.py, I can create a function to scrape any website I want for any sport news I want, and then update sportsnews.py to send that information as an email and template.py to support a template for that category of information. I would then store the mailing list as a new variable in the .env file.

Although I use this project to send daily sports updates, it can be easily configured to send updates at any interval and for any information. 

After initially sending basketball and football updates, I have expanded to project to also send updates for college basketball, college football, cricket, and soccer.

# Functionality

I deployed this project on Heroku, which allows me to automate the process. An email is every morning at 9:00 am for every supported sport to the users on their respective mailing lists. This email contains the latest headlines in the sport from the corresponding website, saving users the time they would spend manually checking the websites themselves. The .env contents are stored as config vars on Heroku, so the exact same program works on both Heroku and my local machine. I also added a link to a google form at the bottom of the email so that users can submit feedback.
