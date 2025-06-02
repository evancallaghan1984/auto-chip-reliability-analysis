import pandas as pd
import numpy as np
from sqlalchemy import create_engine

chip_df = pd.read_csv('automotive_chips_reliability_dataset.csv')
print("Columns: ", chip_df.columns)