import base64
import database
from datetime import date
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from template import sports_template

# delete token.json if modifying scopes
SCOPES = ["https://www.googleapis.com/auth/gmail.send"]

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


def authenticate_email():

    creds = None

    # token.json stores the user's access and refresh tokens
    try:
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    except Exception as e:
        raise e

    return creds


def send_email(sport, creds):

    # gets mailing list from MongoDB
    emails = database.get_mailing_list(sport)
    email_list = ", ".join(emails)

    # creates Gmail API service instance
    service = build("gmail", "v1", credentials=creds)

    # creates email message
    message = MIMEMultipart("alternative")
    message["from"] = "dailysportsheadlines@gmail.com"
    message["to"] = message["from"]
    message["bcc"] = email_list
    message["subject"] = f"Daily {sports[sport]} Update"
    message.attach(MIMEText(sports_template(sport), "html"))
    message = {"raw": base64.urlsafe_b64encode(message.as_string().encode()).decode()}

    try:
        message = service.users().messages().send(userId="me", body=message).execute()
        print(f"successfully sent {sport} email: ", message["id"])
        return message
    except Exception as e:
        raise e


def main():

    # authenticates user
    try:
        creds = authenticate_email()
    except:
        print("failed to authenticate email")

    # sends emails to year-round sports
    for sport in year_round_sports:
        try:
            send_email(sport, creds)
        except Exception as e:
            print(f"failed to send {sport} email: ", e)

    # sends emails to seasonal sports if within season
    for sport in seasonal_sports:
        if times[sport]["start"] <= date.today() <= times[sport]["end"]:
            try:
                send_email(sport, creds)
            except Exception as e:
                print(f"failed to send {sport} email: ", e)


if __name__ == "__main__":
    main()
