import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-here'
    DATA_FOLDER = 'data'
    MEMBERS_FILE = os.path.join(DATA_FOLDER, 'members.csv')
    EVENTS_FILE = os.path.join(DATA_FOLDER, 'events.csv')
    SUBSCRIPTIONS_FILE = os.path.join(DATA_FOLDER, 'subscriptions.csv')