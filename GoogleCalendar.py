# %%
import datetime
import os.path
import pytz

# %%
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# %%
CREDENTIALS_FILE = "client-secret.json"
TOKEN_FILE = "token.json"
SCOPES = ["https://www.googleapis.com/auth/calendar"]

# %%
def create_event(service, summary, start_time, end_time, description= "", location= ""):
    print("creating an event.")
    event = {
        "summary": summary,
        "location": location,
        "description": description,
        "start": {
            "dateTime": start_time.isoformat(),
            "timeZone": "America/Los_Angeles",
        },
        "end": {
            "dateTime": end_time.isoformat(),
            "timeZone": "America/Los_Angeles",
        },
        "reminders":{
            "useDefault": False,
            "overrides": [
                {
                    "method": "email",
                    "minutes": 10
                },
                {
                    "method": "popup",
                    "minutes": 10
                }
            ]
        }
    }

    try:
        event = service.events().insert(calendarId="primary", body=event).execute()
        print(f"Event created: {event.get('htmlLink')}")
        return event
    except HttpError as error:
        print(f"An error occurred: {error}")
        return None

# %%
def get_current_time():

    utc_now = datetime.datetime.now(datetime.timezone.utc)
    pst_offset = datetime.timedelta(hours=-8)
    pst_now = utc_now + pst_offset
    
    return utc_now

# %%
def get_events(service):
    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    print("getting events")
    events_result = (
        service.events()
        .list(
            calendarId='primary',
            timeMin=now,
            maxResults=10,
            singleEvents=True,
            orderBy='startTime'
        )
        .execute()
    )
    events = events_result.get('items', [])

    if not events:
        return ("no events found.")
    else:
        print("Upcoming events:")
        for event in events:
            start = event["start"].get("dateTime")
            if start is None:
                start = event["start"].get("date")
                
            return(f"  {start} - {event["summary"]}")



# %%
def test_event(service):
    now = datetime.datetime.now(datetime.timezone.utc)
    print(now)
    start_time = now + datetime.timedelta(days=1)
    end_time = start_time + datetime.timedelta(hours=1)

    return create_event(
        service,
        summary="Test Event",
        start_time= datetime.datetime.fromisoformat("2025-08-12T13:00:00"),
        end_time=datetime.datetime.fromisoformat("2025-08-12T14:00:00"),
        description="This is a test event",
        location="Virtual"
    )

# %%
def create_calendar_client():
    
    creds = None

    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)

        with open(TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())
    

    try:
        service = build("calendar", "v3", credentials = creds)
        return service

    except HttpError as error:
        print(f"An error occurred: {error}")

# %%
# calendar_client = create_calendar_client()


client = create_calendar_client()
test_event(client)
