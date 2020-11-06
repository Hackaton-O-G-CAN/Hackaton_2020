import pandas as pd
from pathlib import Path
from jinja2 import Template
import os
import matplotlib.pyplot as plt

class generateWeb:
    def __init__(self, df_dict:pd.DataFrame):
        self.df_dict = df_dict

    def parseHTML(self, df_dict:pd.DataFrame):
        """
        """
        self.df_dict = df_dict
        print("Generating HTML")

        assets_dir = Path("./web/assets/")


        if os.path.isdir(assets_dir):
            template_dir = Path('./templates/index.html')
            index_dir = Path('./index.html')

            temp_dir = open(template_dir, 'r').read()
            template = Template(temp_dir)

            self.renderImages(self.df_dict)

            years = [int(year) for year in self.df_dict.keys()]
            years.sort()
            years_sorted = [str(year) for year in years]

            temp_dir = template.render(years=years_sorted)
            open(index_dir, 'w').write(temp_dir)
        else:
            os.mkdir(assets_dir)
            self.parseHTML(df_dict)

    def renderImages(self, df_dict:pd.DataFrame):
        to_drop = ['departamento', 'municipio',
                            'operadora', 'contrato', 'cuenca','campo']
        for year in df_dict.keys():
            for col in to_drop:
                if col in df_dict[year]:
                    df_dict[year] = df_dict[year].drop(labels=[col], axis=1)

            df_dict[year] = df_dict[year].sum(axis =0)/1000000
            df_dict[year] = pd.DataFrame(df_dict[year],columns = ['production']).reset_index()
            df_dict[year] = df_dict[year].rename(columns={0:'month'})
            plt.tight_layout()
            fig = df_dict[year].plot.bar(x='month', y='production',legend=False,ylabel="MMstb",rot=15, title=f"Producción Crudo {year} - [MMstb - Mes]",ylim=(0,2.1)).get_figure().savefig(Path(f'./web/assets/{year}.png'))