from notion_client import Client
from dotenv import load_dotenv
import os
import json

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

# Function to find the first icon in the database
def find_first_icon(database_id):
    response = notion.databases.query(database_id=database_id)
    
    # Print the response for debugging
    print(json.dumps(response, indent=2))
    
    for result in response['results']:
        if 'icon' in result and result['icon'] is not None:
            if 'emoji' in result['icon']:
                return result['icon']['emoji']
    return None

# Find the first icon in the database
first_icon = find_first_icon(database_id)

if first_icon:
    print(f"First found icon: {first_icon}")
    
    # Query the database to get all items
    response = notion.databases.query(database_id=database_id)

    # Iterate over the results and update the icons
    for result in response['results']:
        page_id = result['id']
        update_page_icon(page_id, first_icon)

    print("Icons updated successfully.")
else:
    print("No icons found in the database.")
