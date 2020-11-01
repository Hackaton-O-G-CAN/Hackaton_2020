import os
import re
import urllib.request
from requests import get
from bs4 import BeautifulSoup

class downloadData:
    def __init__(self, url="http://www.anh.gov.co/estadisticas-del-sector/sistemas-integrados-operaciones/estad%C3%ADsticas-producci%C3%B3n"):
        self.url = url
        self.links = None

    def get_links(self) -> list:
        # Get HTML
        response = get(self.url)
        # Parse HTML
        html_soup = BeautifulSoup(response.text, 'html.parser')
        # Get <a href></a> tags
        files_containers = html_soup.find_all('a', href=True)
        # Filter useful tags
        links = [href["href"] if ".xlsx" in str(href) else "" for href in files_containers]
        
        return links

    def get_filenames(self, links:list) -> list:
        filenames = []
        for link in links:
            filenames.append(re.findall(r'[^\/]+(?=\.xlsx$)', link))

        return filenames

    
    def getData(self):
        
        links = self.get_links()
        filenames = self.get_filenames(links)

        if os.path.isdir("./data"):
            for url, filename in zip(links, filenames):
                base_url = "http://www.anh.gov.co"
                full_url =  str(base_url) + str(url)
                output_dir = "./data/" + str(filename[0]) + ".xlsx"

                urllib.request.urlretrieve(full_url, str(output_dir))