import requests
from bs4 import BeautifulSoup

# Step 1: Fetch HTML
URL = 'https://www.bbc.com/news'
response = requests.get(URL)
if response.status_code != 200:
    raise Exception("Failed to load page")

# Step 2: Parse with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Extract headlines (BBC uses <h2> tags for headlines)
headlines = []
for h2_tag in soup.find_all('h2'):
    text = h2_tag.get_text(strip=True)
    if text and text not in headlines:
        headlines.append(text)

# Step 4: Save to .txt file
with open('headlines.txt', 'w', encoding='utf-8') as file:
    for i, headline in enumerate(headlines, start=1):
        file.write(f"{i}. {headline}\n")

print(f"{len(headlines)} headlines saved to 'headlines.txt'.")

