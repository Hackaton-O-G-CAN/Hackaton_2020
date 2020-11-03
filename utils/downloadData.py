import os
import re
import urllib.request
from requests import get
from bs4 import BeautifulSoup
from numpy import arange


class downloadData:
    def __init__(self, url="http://www.anh.gov.co/estadisticas-del-sector/sistemas-integrados-operaciones/estad%C3%ADsticas-producci%C3%B3n"):
        self.url = url

    def get_links(self) -> list:
        try:
            links_clean = []
            # Get HTML
            response = get(self.url)
            # Parse HTML
            html_soup = BeautifulSoup(response.text, 'html.parser')
            # Get <a href></a> tags
            files_containers = html_soup.find_all('a', href=True)
            # Filter useful tags
            links = [href["href"] if (".xlsx" and "crudo") in str(href).lower() else "" for href in files_containers]

            # For each link, clean empty records
            for link in links:
                if link == "":
                    continue
                else:
                    links_clean.append(link)

            return links_clean
        except:
            self.get_links()

    def get_filenames(self, links: list) -> list:
        filenames = []

        # Find filenames before ".xlsx" then clean non matching records
        for link in links:
            file = re.findall(r'[^\/]+(?=\.xlsx$)', link)
            if len(file) == 0:
                continue
            else:
                # Clean non-meaningful characters
                file = file[0].lower().replace('%', '').replace('.', '').replace('-', '').replace('_', '')

                # Extract year and month (three first letters) or simply year from filename and rename it
                if len(re.findall(r'[0-9]{4}[a-z]{3}', file)) == 0:
                    file = re.findall(r'[0-9]{4}$', file)[0]
                else:
                    file = re.findall(r'[0-9]{4}[a-z]{3}', file)[0]
                    if "2019" in file:
                        file = "2019"

            filenames.append(file)

        return filenames

    def getData(self):
        if os.path.isdir("./data"):
            #links = self.get_links()
            links = ['/Operaciones-Regal%c3%adas-y-Participaciones/Sistema-Integrado-de-Operaciones/Documentos%20compartidos/Producci%c3%b3n%20Fiscalizada%20Crudo%202020%20Agosto.xlsx',
                    '/Operaciones-Regal%c3%adas-y-Participaciones/Sistema-Integrado-de-Operaciones/Documentos%20compartidos/Producci%c3%b3n%20Fiscalizada%20Crudo%202020%20Julio.xlsx' ,
                    '/Operaciones-Regal%c3%adas-y-Participaciones/Sistema-Integrado-de-Operaciones/Documents/Producci%c3%b3n%20Fiscalizada%20Crudo%202020%20Junio.xlsx' ,
                    '/Operaciones-Regal%c3%adas-y-Participaciones/Sistema-Integrado-de-Operaciones/Documents/Producci%c3%b3n%20Fiscalizada%20Crudo%202020%20Mayo.xlsx' ,
                    '/Operaciones-Regal%c3%adas-y-Participaciones/Sistema-Integrado-de-Operaciones/Documents/Producci%c3%b3n%20Fiscalizada%20Crudo%202020%20Abril.xlsx' ,
                    '/Operaciones-Regal%c3%adas-y-Participaciones/Sistema-Integrado-de-Operaciones/Documents/Producci%c3%b3n%20Fiscalizada%20Crudo%202020%20Marzo.xlsx' ,
                    '/Operaciones-Regal%c3%adas-y-Participaciones/Sistema-Integrado-de-Operaciones/Documents/Producci%c3%b3n%20Fiscalizada%20Crudo%202020%20ENERO..._.xlsx' ,
                    '/Operaciones-Regal%c3%adas-y-Participaciones/Sistema-Integrado-de-Operaciones/Documents/Producci%c3%b3n%20Fiscalizada%20Crudo%202019-DIC.xlsx' ,
                    '/Operaciones-Regal%c3%adas-y-Participaciones/Sistema-Integrado-de-Operaciones/Documents/Producci%c3%b3n%20Fiscalizada%20Crudo%202018.xlsx' ,
                    '/Operaciones-Regal%c3%adas-y-Participaciones/Sistema-Integrado-de-Operaciones/Documents/Produccion-fiscalizada-crudo-2017.xlsx',
                    '/Operaciones-Regal%c3%adas-y-Participaciones/Sistema-Integrado-de-Operaciones/Documents/Producci%c3%b3n%20Fiscalizada%20Crudo%202015.xlsx' ,
                    '/Operaciones-Regal%c3%adas-y-Participaciones/Sistema-Integrado-de-Operaciones/Documents/Producci%c3%b3n%20fiscalizada%20de%20crudo_2014_31122014.xlsx' ,
                    '/Operaciones-Regal%c3%adas-y-Participaciones/Sistema-Integrado-de-Operaciones/Documents/Producci%c3%b3n%20fiscalizada%20de%20crudo%20a%c3%b1o%202013.xlsx']
            filenames = self.get_filenames(links)

            for url, filename in zip(links, filenames):
                base_url = "http://www.anh.gov.co"
                full_url = f"{base_url}/{url}"
                base_dir = "./data"
                output_dir = f"{base_dir}/{filename}.xlsx"

                if os.path.isfile(output_dir) == True:
                    continue
                else:
                    urllib.request.urlretrieve(full_url, str(output_dir))
        else:
            os.mkdir("./data")
            self.getData()
