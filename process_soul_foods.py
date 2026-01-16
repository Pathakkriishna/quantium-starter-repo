import pandas as pd
import glob

csv_files = glob.glob("data/*.csv")

df_list = []

for file in csv_files:
    df = pd.read_csv(file)
    
    # Strip column names
    df.columns = df.columns.str.strip()
    
    # ing only Pink Morsels
    df = df[df["product"].str.strip().str.lower() == "pink morsel"]
    
    # Converting price and quantity to numeric
    df["price"] = df["price"].replace('[\$,]', '', regex=True).astype(float)
    df["quantity"] = df["quantity"].astype(float)
    
    # Calculateing Sales
    df["Sales"] = df["quantity"] * df["price"]
    
    # Keeping only needed columns
    df = df[["Sales", "date", "region"]]
    df = df.rename(columns={"date": "Date", "region": "Region"})
    
    df_list.append(df)


final_df = pd.concat(df_list, ignore_index=True)

final_df.to_csv("data/pink_morsel_sales.csv", index=False)

print("Processed CSV created successfully!")
