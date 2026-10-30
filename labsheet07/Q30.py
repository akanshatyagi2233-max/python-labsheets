# Program 30: Combine multiple CSV files into one single file
import csv

# Create two sample CSV files to combine
file1_data = [["ID", "Item"], [1, "Pen"], [2, "Pencil"]]
file2_data = [["ID", "Item"], [3, "Notebook"], [4, "Eraser"]]

with open("file1.csv", "w", newline="") as f1:
    csv.writer(f1).writerows(file1_data)
with open("file2.csv", "w", newline="") as f2:
    csv.writer(f2).writerows(file2_data)

# Combine logic
input_files = ["file1.csv", "file2.csv"]
output_file = "combined_files.csv"

try:
    with open(output_file, "w", newline="") as outfile:
        writer = csv.writer(outfile)
        header_written = False

        for fname in input_files:
            with open(fname, "r") as infile:
                reader = csv.reader(infile)
                header = next(reader)  # Read header
                
                # Write header only once
                if not header_written:
                    writer.writerow(header)
                    header_written = True
                
                # Write remaining rows
                for row in reader:
                    writer.writerow(row)

    print("Multiple CSV files successfully combined into 'combined_files.csv'.")

except IOError as e:
    print(f"An I/O error occurred: {e}")
