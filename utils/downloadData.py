import os
import re
import urllib.request
from requests import get
from bs4 import BeautifulSoup

class downloadData:
    def __init__(self, url="http://www.anh.gov.co/estadisticas-del-sector/sistemas-integrados-operaciones/estad%C3%ADsticas-producci%C3%B3n"):
        self.url = url

    def get_links(self) -> list:
        try:
                # Get HTML
            response = get(self.url)
            # Parse HTML
            html_soup = BeautifulSoup(response.text, 'html.parser')
            # Get <a href></a> tags
            files_containers = html_soup.find_all('a', href=True)
            # Filter useful tags
            links = [href["href"] if (".xlsx" and "crudo") in str(href).lower() else "" for href in files_containers]
            
            return links
        except:
            self.get_links()
        
    def get_filenames(self, links:list) -> list:
        filenames = []
        for link in links:
            filenames.append(re.findall(r'[^\/]+(?=\.xlsx$)', link))

        return filenames

    def getData(self):
        
        links=self.get_links()
        filenames = self.get_filenames(links)

        links_clean = []
        filenames_clean = []

        for link in links:
            if link == "":
                continue
            else:
                links_clean.append(link)

        for file in filenames:
            if len(file) == 0:
                continue
            else:
                filenames_clean.append(file)

        if os.path.isdir("./data"):
            for url, filename in zip(links_clean, filenames_clean):
                base_url = "http://www.anh.gov.co"
                full_url =  str(base_url) + str(url)
                output_dir = "./data/" + str(filename[0]) + ".xlsx"

                if os.path.isfile(output_dir) == True:
                    continue
                else:
                    urllib.request.urlretrieve(full_url, str(output_dir))
        else:
            os.mkdir("./data")
            self.getData()