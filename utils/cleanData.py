import pandas as pd
import numpy as np
from glob import glob

class cleanData:
    def __init__(self):
        pass
    def cleanData(self) -> pd.DataFrame:
        pass

    def lss(self, expr = '*.*'):
        return glob(expr)