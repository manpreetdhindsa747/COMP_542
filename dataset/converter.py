# Author - Manpreet Dhindsa
# Author - Ahmed Bin Sultan Bahyal

import csv

def convert(column_headers):
    input_file_name = "adult.data"
    output_file_name = "adult.csv"

    with open(input_file_name, "r") as input_file, open(output_file_name, "w", newline="") as output_file:
        csv_writer = csv.writer(output_file)
        csv_writer.writerow(column_headers)

        for line in input_file:
            data = line.strip().replace(" ", "").split(",")
            csv_writer.writerow(data)

    print(f"Conversion completed. Data saved to '{output_file_name}'.")

def main():
    column_headers = ["age",
                      "workclass",
                      "fnlwgt",
                      "education",
                      "education_num",
                      "marital_status",
                      "occupation",
                      "relationship",
                      "race",
                      "sex",
                      "capital_gain",
                      "capital_loss",
                      "hours_per_week",
                      "native_country",
                      "target"]
    convert(column_headers)

if __name__ == "__main__":
    main()