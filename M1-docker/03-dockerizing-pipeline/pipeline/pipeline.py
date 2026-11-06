import sys
import pandas as pd
from pathlib import Path
from datetime import date, timedelta

print("arguments", sys.argv)

if len(sys.argv) < 2:
    print("Usage: pipeline.py YYYY-MM-DD", file=sys.stderr)
    sys.exit(1)

input_date = date.fromisoformat(sys.argv[1])
print(f"Running pipeline for date {input_date}")

previous_date = input_date - timedelta(days=1)
next_date = input_date + timedelta(days=1)

df = pd.DataFrame({"Input date": [input_date], "Previous date": [previous_date], "Next date": [next_date]})
print(df.head())

output_dir = Path("output")
output_dir.mkdir(parents=True, exist_ok=True)
df.to_parquet(output_dir / f"output_date_{input_date}.parquet")

print(f"Job finished successfully for date = {input_date}")
