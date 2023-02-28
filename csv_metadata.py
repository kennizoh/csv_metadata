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

            # Write the column headers, number of rows and columns to the output file
            out.write("Columns:\n")
            for header in headers:
                out.write(f"  - {header}\n")
            out.write(f"Number of rows: {num_rows}\n")
            out.write(f"Number of columns: {num_cols}\n")
            out.write("Data types:\n")

            # Re-open the CSV file for reading from the beginning
            csvfile.seek(0)
            reader = csv.reader(csvfile)

            # Skip the header row
            next(reader)

            # Read one row to infer the data types of each column
            sample_row = next(reader)

            # Infer the data type of each column and write it to the output file
            col_types = []
            for i, value in enumerate(sample_row):
                if value == '':
                    col_type = type(None)
                else:
                    try:
                        col_type = type(int(value))
                    except ValueError:
                        try:
                            col_type = type(float(value))
                        except ValueError:
                            col_type = type(value)
                col_types.append(col_type)
                out.write(f"  - {headers[i]}: {col_type}\n")

            # Add a blank line after the metadata for each file
            out.write("\n")
