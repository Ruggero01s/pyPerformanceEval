import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Function to read CSV file and return a pandas DataFrame
def read_csv_to_dataframe(file_path):
    try:
        df = pd.read_csv(file_path)
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


# Main function to read the CSV and plot the data
def main():
    order = 2

    file_path = 'output.csv'  # Update this with your file path
    df = read_csv_to_dataframe(file_path)

    if df is not None:
        print("DataFrame head:")
        print(df.head())

        # Update these columns to match your data
        x_column = 'name'
        y_column = 'execution_time'

        plt.figure(figsize=(10, 6))
        df.plot(x=x_column, y=y_column, kind='box')
        plt.title(x_column + " vs " + y_column)
        plt.legend()
        plt.grid(True)
        plt.show()

        x_column = 'name'
        y_column = 'memory_occupation'
        # Plot occupazione spaziale massima vs dimensione matrice
        plt.figure(figsize=(10, 6))
        df.plot(x=x_column, y=y_column, kind='box')
        plt.title(x_column + " vs " + y_column)
        plt.legend()
        plt.grid(True)
        plt.show()

        # x_column = 'matrix_size'
        # y_column = 'num_explored_hypotheses'
        # # Plot numero di ipotesi esplorate vs dimensione matrice
        # plt.figure(figsize=(10, 6))
        # sns.lmplot(x=x_column, y=y_column, data=df, fit_reg=True, order=order)
        # plt.title(x_column + " vs " + y_column)
        # plt.legend()
        # plt.grid(True)
        # plt.show()

        # x_column = 'matrix_size'
        # y_column = 'num_solutions'
        # # Plot numero di soluzioni trovate vs dimensione matrice
        # plt.figure(figsize=(10, 6))
        # sns.lmplot(x=x_column, y=y_column, data=df, fit_reg=True, order=order)
        # plt.title(x_column + " vs " + y_column)
        # plt.legend()
        # plt.grid(True)
        # plt.show()

        # x_column = 'num_explored_hypotheses'
        # y_column = 'execution_time'
        # # Plot numero di soluzioni trovate vs dimensione matrice
        # plt.figure(figsize=(10, 6))
        # sns.lmplot(x=x_column, y=y_column, data=df, fit_reg=True, order=order)
        # plt.title(x_column + " vs " + y_column)
        # plt.legend()
        # plt.grid(True)
        # plt.show()

        # x_column = 'num_explored_hypotheses'
        # y_column = 'memory_occupation'
        # # Plot numero di soluzioni trovate vs dimensione matrice
        # plt.figure(figsize=(10, 6))
        # sns.lmplot(x=x_column, y=y_column, data=df, fit_reg=True, order=order)
        # plt.title(x_column + " vs " + y_column)
        # plt.legend()
        # plt.grid(True)
        # plt.show()


        # pivot_table = df.pivot(index="matrix_size", columns="execution_time", values="num_solutions")
        # # Plot numero di soluzioni trovate vs dimensione matrice
        # plt.figure(figsize=(10, 6))
        # sns.heatmap(pivot_table, fmt="d", cmap="YlGnBu")
        # plt.title(x_column + " vs " + y_column)
        # plt.show()



if __name__ == "__main__":
    main()
