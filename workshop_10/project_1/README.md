install virtualenv package
```bash
pip install virtualenv
```
1. create a virtual environment
```bash
virtualenv .venv
```
2. activate the virtual environment
```bash
source .venv/bin/activate
```

```pwsh
.\.venv\Scripts\Activate.ps1
```

```cmd
.\.venv\Scripts\activate.bat
```


3. install the required packages
```bash
pip install pandas matplotlib
```
4. run the main script

we used someone else's code to analyze and visualize the data. The code reads a CSV file containing transaction data, calculates some statistics, and plots a graph of total transactions against total transactions in.
