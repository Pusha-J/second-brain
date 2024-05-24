from notion_client import Client
from dotenv import load_dotenv
import os
from collections import Counter

# Load environment variables from .env file
load_dotenv()

# Initialize the Notion client with your integration token
notion = Client(auth=os.getenv("NOTION_INTEGRATION_TOKEN"))

# Define your database ID
database_id = os.getenv("DATABASE_ID")

# Print environment variables for debugging
print(f"Using NOTION_INTEGRATION_TOKEN: {os.getenv('NOTION_INTEGRATION_TOKEN')}")
print(f"Using DATABASE_ID: {database_id}")

# Function to update the icon of a page
def update_page_icon(page_id, icon):
    notion.pages.update(
        page_id=page_id,
        icon={
            "type": "emoji",
            "emoji": icon
        }
    )

# Query the database to get the last 5 items
response = notion.databases.query(database_id=database_id, page_size=5)

# Extract icons from the last 5 tasks
icons = [result['icon']['emoji'] for result in response['results'] if 'icon' in result and 'emoji' in result['icon']]

# Determine the most frequently used icon
most_common_icon = Counter(icons).most_common(1)[0][0] if icons else None

if most_common_icon:
    print(f"Most common icon: {most_common_icon}")
    
    # Query the database to get all items
    response = notion.databases.query(database_id=database_id)

    # Iterate over the results and update the icons
    for result in response['results']:
        page_id = result['id']
        update_page_icon(page_id, most_common_icon)

    print("Icons updated successfully.")
else:
    print("No icons found in the last 5 tasks.")
