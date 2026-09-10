import requests
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize

def load_scripts(url):
    """
    Load scripts from a given URL.
    """
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        script = soup.find('div', attrs={'class': 'scrolling-script-container'}).get_text()
        return script
    else:
        print(f"Failed to retrieve script from {url}. Status code: {response.status_code}.")
        exit()
        
def clean_script(script):
    """
    Clean the script by removing unnecessary whitespace and formatting.
    """
    cleaned_script = script.replace('|', ' ')
    cleaned_script = ' '.join(cleaned_script.split()) # Remove extra whitespace
    return cleaned_script

def split_script_into_chunks(script, title, chunk_size=10, overlap=2):
    """
    Split the script into chunks of a specified size (sentences).
    """
    sentences = sent_tokenize(script)
    chunks = []
    for i in range(0, len(sentences), chunk_size - overlap):
        chunk = ' '.join(sentences[i:i + chunk_size])
        chunks.append({
            "title": title,
            "text": chunk
        })
    return chunks

def save_script_to_file(script, title):
    """
    Save the cleaned script to a text file.
    """
    filename = f"{title.replace(' ', '_')}.txt"
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(script)