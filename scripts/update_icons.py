from notion_client import Client
import os

# Initialize the Notion client with your integration token
notion = Client(auth=os.getenv("NOTION_INTEGRATION_TOKEN"))

# Define your database ID
database_id = os.getenv("DATABASE_ID")

# Define the icons and their corresponding criteria
icons = {
    "Urgent": "🔴",
    "Review": "📘",
    "Follow-up": "🔄"
}

# Function to update the icon of a page
def update_page_icon(page_id, icon):
    notion.pages.update(
        page_id=page_id,
        icon={
            "type": "emoji",
            "emoji": icon
        }
    )

# Query the database to get all tasks
response = notion.databases.query(
    **{
        "database_id": database_id
    }
)

# Iterate over the results and update the icons
for result in response['results']:
    task_name = result['properties']['Name']['title'][0]['text']['content']
    page_id = result['id']
    
    # Determine the icon based on task name or other criteria
    for key in icons:
        if key in task_name:  # Replace with your logic for assigning icons
            update_page_icon(page_id, icons[key])
            break

print("Icons updated successfully.")
