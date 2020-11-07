import os
import pandas as pd
from pathlib import Path
from jinja2 import Template


class generateWeb:
    def __init__(self, df_dict: pd.DataFrame):
        """
        Constructor
        """
        self.df_dict = df_dict

    def parseHTML(self, df_dict: pd.DataFrame):
        """
        Generates index.html, model.html files used in web interface.
        """
        assets_dir = Path("./web/assets/")

        if os.path.isdir(assets_dir):
            print("Generating web interface")
            templates = ["index.html", "model.html"]

            self.renderImages(self.df_dict)

            years = [int(year) for year in self.df_dict.keys()]
            years.sort()
            years_sorted = [str(year) for year in years]

            camps = ["campo1", "campo2"]

            for template_str in templates:
                temp_dir = open(f'templates/{template_str}', 'r').read()
                template = Template(temp_dir)

                if "index" not in template_str:
                    temp_dir = template.render(camps=camps)
                    open(Path(f"./web/{template_str}"), 'w').write(temp_dir)
                else:
                    temp_dir = template.render(years=years_sorted)
                    open('index.html', 'w').write(temp_dir)
            print("Web interface generated")
        else:
            os.mkdir(assets_dir)
            self.parseHTML(self.df_dict)

    def renderImages(self, df_dict: pd.DataFrame):
        """
        """
        print("Rendering images")
        # Non-numerical columns to be dropped
        to_drop = ['departamento', 'municipio',
                   'operadora', 'contrato', 'cuenca', 'campo']
        # Aggregates the data to generate the figures
        for year in self.df_dict.keys():
            for col in to_drop:
                if col in df_dict[year]:
                    df_dict[year] = df_dict[year].drop(labels=[col], axis=1)

            df_dict[year] = df_dict[year].sum(axis=0)/1000000
            df_dict[year] = pd.DataFrame(df_dict[year], columns=[
                                         'production']).reset_index()
            df_dict[year] = df_dict[year].rename(columns={0: 'month'})
            fig = df_dict[year].plot.bar(x='month', y='production', legend=False, xlabel="", ylabel="MMstb", rot=20,title=f"Producción Crudo {year}", ylim=(0, 2.1)).get_figure().savefig(Path(f'./web/assets/{year}.png'))
        print("Images rendered")
