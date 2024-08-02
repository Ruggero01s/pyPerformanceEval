import pandas as pd
from ydata_profiling import ProfileReport


def clean_time(seq_string):
    return list(map(float, seq_string.replace("[", "").replace("]", "").replace("\"", "").split(",")))


def clean_hypotheses(seq_string):
    return list(map(int, seq_string.replace("[", "").replace("]", "").replace("\"", "").split(",")))


# Function to read CSV file and return a pandas DataFrame
def read_csv_to_dataframe(file_path):
    try:
        df = pd.read_csv(file_path, header=0, converters={'per_level_time': clean_time, 'per_level_hypotheses': clean_hypotheses})
        print("CSV file successfully read into a DataFrame!")
        return df
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
    except pd.errors.ParserError:
        print("Error: There was a parsing error with the file.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Main function to read and analyze the data
def main():
    file_path = 'output.csv'  # Update this with your file path
    df = read_csv_to_dataframe(file_path)
    print(df.head())
    print(df.dtypes)
    print(df['per_level_time'])
    profile = ProfileReport(df, title="ProfileReport", explorative=True)
    profile.to_file('analysis.html')


if __name__ == "__main__":
    main()
