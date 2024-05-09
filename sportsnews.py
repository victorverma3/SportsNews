# imports
import database
from datetime import date
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import smtplib
from template import sports_template

# setup
load_dotenv()

# sports
sports = {
    "basketball": "Basketball",
    "cbasketball": "College Basketball",
    "cfootball": "College Football",
    "cricket": "Cricket",
    "football": "Football",
    "soccer": "Soccer",
}

# designated year-round sports
year_round_sports = ["basketball", "cricket", "football", "soccer"]

# designated seasonal sports
seasonal_sports = list(filter(lambda x: x not in year_round_sports, sports.keys()))

# seasonal sport windows
times = {
    "cbasketball": {"start": date(2023, 11, 1), "end": date(2024, 4, 10)},
    "cfootball": {"start": date(2023, 8, 20), "end": date(2024, 1, 15)},
}


# sends email
def sendEmail(sport):

    # gets mailing list
    emails = database.get_mailing_list(sport)

    # constructs email
    msg = MIMEMultipart("alternative")
    msg["From"] = "dailysportsupdate@outlook.com"
    msg["To"] = msg["From"]
    msg["Bcc"] = emails
    msg["Subject"] = f"Daily {sports[sport]} Update"
    msg.attach(MIMEText(sports_template(sport), "html"))

    # sends email
    pswd = os.environ.get("EMAIL_PASSWORD")
    try:
        with smtplib.SMTP(
            "smtp-mail.outlook.com", 587
        ) as s:  # establishes a connection to the hotmail server
            s.ehlo()  # hostname to send for this command defaults to the fully qualified domain name of the local host
            s.starttls()  # puts connection to SMTP server in TLS mode
            s.ehlo()
            s.login(msg["From"], pswd)  # logs into the email account remotely
            s.send_message(msg)
        print(f"\nsuccessfully sent {sport} email")
    except:
        print(f"\nfailed to send {sport} email")


if __name__ == "__main__":

    # sends emails to year-round sports
    for sport in year_round_sports:
        sendEmail(sport)

    # sends emails to seasonal sports if within season
    for sport in seasonal_sports:
        if times[sport]["start"] <= date.today() <= times[sport]["end"]:
            sendEmail(sport)
