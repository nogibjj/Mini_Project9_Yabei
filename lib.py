# This is the main script for IDS706 mini project 2
# In the main.py, the code will read a csv dataset and return a data summary

# the code start here

# loading packages
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



def load_data(data_path):
    my_data = pd.read_csv(data_path, sep=';')
    return my_data


def data_summary(data):
    main_sum = data.describe()
    return main_sum


def data_visual(data):
    sns.set_theme(style="ticks", palette="pastel")
    sns.boxplot(x = 'Origin', y = 'Weight',
                palette="Blues", data = data)
    plt.show()
def main():
    my_df = load_data("cars.csv")
    print(data_summary(my_df))
    data_visual(my_df)


if __name__ == "__main__":
    main()