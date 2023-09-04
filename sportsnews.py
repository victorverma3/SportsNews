# Imports
from datetime import date
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import smtplib
from template import *

# Setup
load_dotenv()
pswd = os.environ.get("hotmail_password")

sports = {
    "basketball": "Basketball",
    "cbasketball": "College Basketball",
    "cfootball": "College Football",
    "cricket": "Cricket",
    "football": "Football",
    "soccer": "Soccer",
}

year = ["basketball", "cricket", "football", "soccer"]  # designated year-round sports
seasonal = list(
    filter(lambda x: x not in year, sports.keys())
)  # designated seasonal sports
times = {
    "cbasketball": {"start": date(2023, 11, 1), "end": date(2024, 4, 10)},
    "cfootball": {"start": date(2023, 8, 20), "end": date(2024, 1, 15)},
}


# Email
def sendEmail(sport, emails):
    """This function sends an email summarizing NFL and NBA headlines to a mailing list."""

    msg = MIMEMultipart("alternative")
    msg["From"] = "dailysportsupdate@outlook.com"  # email sender
    msg["To"] = msg["From"]
    msg["Bcc"] = emails  # email receipients
    msg["Subject"] = f"Daily {sports[sport]} Update"  # email subject line
    msg.attach(MIMEText(template(sport), "html"))  # attaches the html template to email

    with smtplib.SMTP(
        "smtp-mail.outlook.com", 587
    ) as s:  # establishes a connection to the hotmail server
        s.ehlo()  # hostname to send for this command defaults to the fully qualified domain name of the local host
        s.starttls()  # puts connection to SMTP server in TLS mode
        s.ehlo()
        s.login(msg["From"], pswd)  # logs into the email account remotely
        s.send_message(msg)


if os.environ.get("call") == "1":
    if __name__ == "__main__":
        for sport in year:  # sends emails to designated year-round sports
            sendEmail(sport, os.environ.get(f"{sport}List"))
        for (
            sport
        ) in seasonal:  # sends emails to designated seasonal sports if within season
            if times[sport]["start"] <= date.today() <= times[sport]["end"]:
                sendEmail(sport, os.environ.get(f"{sport}List"))
os.environ.pop("call", None)
