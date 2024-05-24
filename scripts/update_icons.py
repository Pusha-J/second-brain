from notion_client import Client
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize the Notion client with your integration token
notion = Client(auth=os.getenv("NOTION_INTEGRATION_TOKEN"))

# Define your database ID
database_id = os.getenv("DATABASE_ID")

# Print environment variables for debugging
print(f"Using NOTION_INTEGRATION_TOKEN: {os.getenv('NOTION_INTEGRATION_TOKEN')}")
print(f"Using DATABASE_ID: {database_id}")

# Define the icon to be used (checkmark square emoji)
icon = "🗹"

# Function to update the icon of a page
def update_page_icon(page_id, icon):
    notion.pages.update(
        page_id=page_id,
        icon={
            "type": "emoji",
            "emoji": icon
        }
    )

# Query the database to get all items
response = notion.databases.query(
    database_id
)

# Iterate over the results and update the icons
for result in response['results']:
    page_id = result['id']
    update_page_icon(page_id, icon)

print("Icons updated successfully.")
