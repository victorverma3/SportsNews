# imports
from dotenv import load_dotenv
import os
import pymongo

# setup
load_dotenv()
client = pymongo.MongoClient(os.environ.get("mongoDBURI"))
db = client["sportsnews-db"]


# adds an email to a sport's mailing list
def add_email(sport, email):
    if db[f"{sport}-list"].find_one({"email": email}):
        print(f"{email} already exists in the mailing list")
    else:
        db[f"{sport}-list"].insert_one({"email": email})
        print(f"added {email} to the mailing list")


# removes an email from a sport's mailing list
def remove_email(sport, email):
    result = db[f"{sport}-list"].delete_one({"email": email})
    if result.deleted_count > 0:
        print(f"Removed {email} from the mailing list")
    else:
        print(f"{email} not found in the mailing list")


# gets all emails in a sport's mailing list
def get_mailing_list(sport):
    emails = [doc["email"] for doc in db[f"{sport}-list"].find({})]
    return emails
