import os
import re
import requests

from numpy import arange
from pathlib import Path
from requests import get
from bs4 import BeautifulSoup



class downloadData:
    def __init__(self, url="http://www.anh.gov.co/estadisticas-del-sector/sistemas-integrados-operaciones/estad%C3%ADsticas-producci%C3%B3n"):
        """
        Initializes the object meant to scrape the excel files.
        """
        self.url = url

    def get_links(self) -> list:
        """
        Return list of links to be downloaded.
        The current module scrape the data from ANH web page,
        gets the crude oil excel files, cleans and return a list of
        links to be downloaded.
        """
        try:
            print("Scrapping started")
            links_clean = []
            # Get HTML
            response = get(self.url)
            # Parse HTML
            html_soup = BeautifulSoup(response.text, 'html.parser')
            # Get <a href></a> tags
            files_containers = html_soup.find_all('a', href=True)
            # Filter useful tags
            links = [href["href"] if (((".xls") and ("crudo")) in str(href).lower()) else "" for href in files_containers]

            # For each link, clean empty records
            for link in links:
                if link == "":
                    continue
                else:
                    links_clean.append(link)
            print("Scrapping finished")
            return links_clean

        except:
            print("Scrapping Failed. Trying again")
            self.get_links()

    def get_filenames(self, links: list) -> list:
        """
        Returns a list of filenames.
        Extract the filenames of the links:list provided.
        """
        self.links = links
        filenames = []
        # Find filenames before ".xlsx" then clean non matching records
        for link in links:
            file = re.findall(r'[^\/]+(?=\.)', link)
            if len(file) == 0:
                continue
            else:
                # Clean non-meaningful characters
                file = file[0].lower().replace('%', '').replace('.', '').replace('-', '').replace('_', '')

                # Extract year and month (three first letters) or simply year from filename and rename it
                if len(re.findall(r'[0-9]{6}',file)) != 0 and "202016" in re.findall(r'[0-9]{6}',file)[0]:
                    file = "2016"
                elif len(re.findall(r'[0-9]{4}[a-z]{3}', file)) == 0:
                    file = re.findall(r'[0-9]{4}$', file)[0]
                else:
                    file = re.findall(r'[0-9]{4}[a-z]{3}', file)[0]
                    if "2019" in file:
                        file = "2019"

            filenames.append(file)
        return filenames

    def getData(self):
        """
        Download the crude oil excel files to the directory "./data"
        """
        # Added a parser (Path) for linux and Windows directories
        base_dir = Path("./data")

        if os.path.isdir(base_dir):
            links = self.get_links()
            filenames = self.get_filenames(links)

            for url, filename in zip(links, filenames):
                base_url = "http://www.anh.gov.co"
                full_url = f"{base_url}{url}"
                if "2016" in filename:
                    output_dir = Path(f"./{base_dir}/{filename}.xls")
                else:
                    output_dir = Path(f"./{base_dir}/{filename}.xlsx")

                if os.path.isfile(output_dir) == True:
                    continue
                else:
                    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"}
                    MAX_RETRIES = 20
                    session = requests.Session()
                    adapter = requests.adapters.HTTPAdapter(max_retries=MAX_RETRIES)
                    session.mount('https://', adapter)
                    session.mount('http://', adapter)

                    data = session.get(full_url, timeout=15, allow_redirects=True, headers=headers)
                    open(output_dir, 'wb').write(data.content)
        else:
            os.mkdir(base_dir)
            self.getData()
        print("Files downloaded")