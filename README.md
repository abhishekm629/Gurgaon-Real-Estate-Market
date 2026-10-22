# Gurgaon Real Estate Analysis

A small Python project that cleans a Gurgaon property listings dataset, prints summary comparisons, and visualizes how property area relates to price and rate per square foot.

## Project files

- `main.py` — data cleaning, analysis, printed results, and scatter plots.
- `realestate_data.csv` — property listings used by the script.

## Requirements

- Python 3
- pandas
- matplotlib
- seaborn

Install the dependencies with:

```bash
python -m pip install pandas matplotlib seaborn
```

## Run

Keep `main.py` and `realestate_data.csv` in the same directory, then run the script from that directory:

```bash
python main.py
```

The script prints:

- The costliest flat in the dataset.
- The localities with the highest average price and average rate per square foot.
- Average-price comparisons by construction status and RERA approval.
- The BHK configuration and property type with the highest average rate per square foot.
- The five builders with the highest average rate per square foot.

It also opens scatter plots for area versus price and area versus rate per square foot.

## Data processing

The script standardizes column names and selected text fields, converts price, area, and rate-per-square-foot values to numbers, maps RERA approval values to booleans, and removes duplicate rows before calculating results.

The input CSV should contain the property fields used by the analysis, including `Price`, `Status`, `Area`, `Rate per sqft`, `Property Type`, `Locality`, `RERA Approval`, `BHK_Count`, and `Company Name`.
