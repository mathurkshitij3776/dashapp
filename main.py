import csv
import os

# 1. Define input and output file paths
input_filenames = [
    'data/daily_sales_data_0.csv', 
    'data/daily_sales_data_1.csv', 
    'data/daily_sales_data_2.csv'
]

output_filename = 'formatted_data.csv'

# 2. Open the output file in write mode
# 'newline=""' is important to prevent blank lines between rows in Windows
with open(output_filename, 'w', newline='') as output_file:
    csv_writer = csv.writer(output_file)
    
    # 3. Write the required header row
    csv_writer.writerow(['Sales', 'Date', 'Region'])

    print("Processing files...")

    # 4. Loop through each input file
    for filename in input_filenames:
        try:
            with open(filename, 'r') as csv_file:
                csv_reader = csv.reader(csv_file)
                
                # Skip the input file's header (product, price, quantity, date, region)
                header = next(csv_reader)
                
                for row in csv_reader:
                    product_name = row[0]
                    
                    # 5. Filter: We only want 'pink morsel'
                    if product_name == 'pink morsel':
                        
                        # Extract data (row[1] is price, row[2] is quantity, row[3] is date, row[4] is region)
                        # We must strip the '$' from price to multiply it
                        price = float(row[1].strip('$'))
                        quantity = int(row[2])
                        
                        # Calculate Sales
                        sales = price * quantity
                        
                        date = row[3]
                        region = row[4]
                        
                        # 6. Write the transformed row to the output file
                        csv_writer.writerow([sales, date, region])
                        
            print(f"-> Successfully processed {filename}")
            
        except FileNotFoundError:
            print(f"Error: Could not find {filename}. Please ensure the 'data' folder exists and contains the files.")

print(f"Done! Check '{output_filename}' for the results.")