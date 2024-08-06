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

    file_path = 'output_perms.csv'  # Update this with your file path
    df = read_csv_to_dataframe(file_path)
    graph_path = "graphs/"
    if df is not None:
        print("DataFrame head:")
        print(df.head())

        # Permutations benchmark graphs
        draw_graph(data=df, x_column="name", y_column="execution_time", path=graph_path, kind="scatter", regression=False, order=order)
        draw_graph(data=df, x_column="name", y_column="memory_occupation", path=graph_path, kind="scatter", regression=False, order=order)
        draw_graph(data=df, x_column="name", y_column="execution_time", path=graph_path, kind="box", regression=False, order=order)
        draw_graph(data=df, x_column="name", y_column="memory_occupation", path=graph_path, kind="box", regression=False, order=order)

        # Benchmark graphs
        # draw_graph(data=df, x_column="matrix_size", y_column="num_explored_hypotheses", path=graph_path, kind="scatter",
        #            regression=True, order=order)
        # draw_graph(data=df, x_column="|N|", y_column="num_explored_hypotheses", path=graph_path, kind="scatter",
        #            regression=True, order=order)
        # draw_graph(data=df, x_column="|M1|", y_column="num_explored_hypotheses", path=graph_path, kind="scatter",
        #            regression=True, order=order)
        # draw_graph(data=df, x_column="matrix_size", y_column="num_solutions", path=graph_path, kind="scatter",
        #            regression=True, order=order)
        # draw_graph(data=df, x_column="|N|", y_column="num_solutions", path=graph_path, kind="scatter",
        #            regression=True, order=order)
        # draw_graph(data=df, x_column="|M1|", y_column="num_solutions", path=graph_path, kind="scatter",
        #            regression=True, order=order)
        # draw_graph(data=df, x_column="num_explored_hypotheses", y_column="execution_time", path=graph_path,
        #            kind="scatter", regression=True, order=order)
        # draw_graph(data=df, x_column="num_explored_hypotheses", y_column="memory_occupation", path=graph_path,
        #            kind="scatter", regression=True, order=order)
        # draw_graph(data=df, x_column="num_explored_hypotheses", y_column="hypotheses_per_second", path=graph_path,
        #            kind="scatter", regression=True, order=order)
        # draw_graph(data=df, x_column="matrix_size", y_column="hypotheses_per_second", path=graph_path, kind="scatter",
        #            regression=True, order=order)
        # draw_graph(data=df, x_column="|N|", y_column="hypotheses_per_second", path=graph_path, kind="scatter",
        #            regression=True, order=order)
        # draw_graph(data=df, x_column="|M1|", y_column="hypotheses_per_second", path=graph_path, kind="scatter",
        #            regression=True, order=order)


def draw_graph(x_column, y_column, kind, data, path, regression, order):
    if kind == "box":
        # Plot occupazione spaziale massima vs dimensione matrice
        plt.figure(figsize=(10, 8))
        plot = data.plot(x=x_column, y=y_column, kind='box')
        plt.title(x_column + " vs " + y_column)
        plt.grid(True)
        fig = plot.get_figure()
        fig.legend()
        fig.tight_layout()
        fig.show()
        fig.savefig(path + x_column.strip("|") + " vs " + y_column.strip("|") + " box.png", dpi=400, transparent=True,
                    bbox_inches='tight')
    elif kind == "scatter":
        plt.figure(figsize=(10, 8))
        if regression:
            plot = sns.lmplot(x=x_column, y=y_column, data=data, fit_reg=True, order=order)
        else:
            plot = data.plot(x=x_column, y=y_column, kind='scatter', rot=90)
        plt.title(x_column + " vs " + y_column)
        plt.grid(True)
        # per togliere i nomi dei dati delle x
        # plt.xticks([])
        if regression:
            fig = plot.fig
        else:
            fig = plot.get_figure()

        fig.legend()
        fig.tight_layout()
        fig.show()
        fig.savefig(path + x_column.strip("|") + " vs " + y_column.strip("|") + " scatter.png", dpi=400,
                    transparent=True,
                    bbox_inches='tight')


if __name__ == "__main__":
    main()
