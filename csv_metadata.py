import csv
import os

# Define the output file
output_file = "metadata.txt"

# Get the list of CSV files in the current directory
csv_files = [filename for filename in os.listdir(".") if filename.endswith(".csv")]

# Open the output file for writing
with open(output_file, "w") as out:

    # Loop through each CSV file
    for csv_file in csv_files:

        # Write the file name as a section header
        out.write(f"Metadata for {csv_file}:\n")

        # Open the CSV file for reading
        with open(csv_file, "r") as csvfile:

            # Use the csv module to read the CSV file
            reader = csv.reader(csvfile)

            # Read the column headers, count the number of rows and columns
            headers = next(reader)
            num_rows = sum(1 for row in reader) + 1
            num_cols = len(headers)

            # Write the column headers, data types, number of rows and columns to the output file
            out.write("Columns:\n")
            for header in headers:
                out.write(f"  - {header}\n")
            out.write("Data types:\n")
            for row in reader:
                for i, value in enumerate(row):
                    if value == '':
                        out.write(f"  - {type(None)}\n")
                    else:
                        try:
                            out.write(f"  - {type(int(value))}\n")
                        except ValueError:
                            try:
                                out.write(f"  - {type(float(value))}\n")
                            except ValueError:
                                out.write(f"  - {type(value)}\n")
                break  # Read only one row to infer data types

            out.write(f"Number of rows: {num_rows}\n")
            out.write(f"Number of columns: {num_cols}\n")

            # Add a blank line after the metadata for each file
            out.write("\n")
