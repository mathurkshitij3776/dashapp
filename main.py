import csv
import os

# Updated to look inside the 'data' folder with the correct filenames
filenames = [
    'data/daily_sales_data_0.csv', 
    'data/daily_sales_data_1.csv', 
    'data/daily_sales_data_2.csv'
]

total_sales = 0
files_processed = 0

for filename in filenames:
    try:
        with open(filename, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            header = next(csv_reader) # Skip header
            
            for row in csv_reader:
                if row[0] == 'pink morsel':
                    
                    price = float(row[1].strip('$'))
                    quantity = int(row[2])
                    total_sales += price * quantity
            
            files_processed += 1
            print(f"Successfully processed: {filename}")
            
    except FileNotFoundError:
        # This will help us confirm exactly what is failing
        print(f"Error: Could not find '{filename}' in directory '{os.getcwd()}'")

if files_processed == 0:
    print("\n--- TROUBLESHOOTING ---")
    print("No files were found. Here are the files actually located in your 'data' folder:")
    if os.path.exists('data'):
        print(os.listdir('data'))
    else:
        print("The 'data' folder does not exist in this directory.")
else:
    print(f"Total Sales for Pink Morsel: ${total_sales:,.2f}")