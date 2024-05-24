# second-brain


## We will add more functionality to this by prompting notion with this prompt:

## Prompt for Expanding Script Functionality

### Context:
We developed a script to update icons for all tasks in my Notion database using the URL: `https://www.notion.so/icons/checkmark-square_gray.svg`. The script is integrated with GitHub Actions and successfully applies the specified icon to all tasks. The current workflow includes the following:

1. **Script (`update_icons.py`)**:
   - Initializes the Notion client.
   - Queries the database for all tasks.
   - Updates the icon for each task.

2. **GitHub Actions Workflow (`main.yml`)**:
   - Sets up the environment.
   - Installs necessary dependencies.
   - Runs the script to update icons.

### Future Expansion Goals:
1. **Extend Icon Updates to Notes Database**:
   - Modify the script to update icons not only in the task database but also in the notes database.

2. **Icon Updates Based on Note Type**:
   - In the notes database, differentiate between types of notes (e.g., text notes, video notes).
   - Apply specific icons based on the note type (e.g., check if there's a URL attached, and if the URL contains "youtube" for video notes).

3. **Trigger Workflow on Database Changes**:
   - Explore ways to trigger this workflow whenever a change is detected in the Notion database, such as when a new item is added to the notes or tasks databases.

### Reference:
Here's the current script and workflow setup:

**Script (`update_icons.py`):**
```python
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

# Define the icon URL to be used
icon_url = "https://www.notion.so/icons/checkmark-square_gray.svg"

# Function to update the icon of a page
def update_page_icon(page_id, icon_url):
    notion.pages.update(
        page_id=page_id,
        icon={
            "type": "external",
            "external": {
                "url": icon_url
            }
        }
    )

# Query the database to get all items
response = notion.databases.query(database_id=database_id)

# Iterate over the results and update the icons
for result in response['results']:
    page_id = result['id']
    update_page_icon(page_id, icon_url)

print("Icons updated successfully.")
```

**GitHub Actions Workflow (`main.yml`):**
```yaml
name: Update Notion Icons

on:
  schedule:
    - cron: '0 * * * *' # Runs every hour, adjust as needed
  workflow_dispatch:

jobs:
  update_icons:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install notion-client python-dotenv

      - name: List scripts directory contents
        run: ls -R scripts

      - name: Run the script
        run: python scripts/update_icons.py
        env:
          NOTION_INTEGRATION_TOKEN: ${{ secrets.NOTION_INTEGRATION_TOKEN }}
          DATABASE_ID: ${{ secrets.DATABASE_ID }}
```
