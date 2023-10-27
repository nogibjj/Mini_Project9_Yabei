# import pandas as pd
from lib import load_data, data_summary, data_visual

def main():

    data_path = "https://raw.githubusercontent.com/yabeizeng1121/Mini_Project5/main/cars.csv"
    df = load_data(data_path)
    sum_data = data_summary(df)

    print(sum_data)
    data_visual(df)


if __name__ == "__main__":
    main()
