from pathlib import Path
import pandas as pd
import matplotlib

# we resolve absolute Path from file
BASE_DIR = Path(__file__).parent
DATA_FILE = BASE_DIR / "nft_data.csv"
print(BASE_DIR.parent, BASE_DIR)

print(DATA_FILE)

# with DATA_FILE.open("r") as f:
#     pass

# someone wrote all this functions in pandas package and we use it
df = pd.read_csv(DATA_FILE)

print(df.head(10))
print(df.tail(10))

print(df["total_tx"].mean())
print(df["total_tx_in"].mean())
print(df["total_tx_out"].mean())

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
df.plot(x="total_tx", y="total_tx_in", kind="line")
plt.show()
