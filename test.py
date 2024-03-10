import sys
print(sys.executable)

import pandas as pd

df = pd.DataFrame({"a": range(5)})
print(df)


df.describe()
