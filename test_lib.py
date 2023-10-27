from lib import data_summary, load_data, data_visual
import pandas as pd

def test_summary():
    my_df = pd.read_csv('https://raw.githubusercontent.com/yabeizeng1121/Mini_Project5/main/cars.csv', sep=';')
    summary = data_summary(my_df)
    mean = my_df['Weight'].mean()
    median = my_df['Weight'].median()
    assert mean == summary.loc['mean', 'Weight'], "Mean test failed"
    assert median == summary.loc['50%', 'Weight'], "Median test failed"

def test_load_data():
    data_path = 'https://raw.githubusercontent.com/yabeizeng1121/Mini_Project5/main/cars.csv'
    df = load_data(data_path)
    assert isinstance(df, pd.DataFrame), "load_data should return a DataFrame"
    assert not df.empty, "DataFrame should not be empty"

def test_data_visual():
    data_path = 'https://raw.githubusercontent.com/yabeizeng1121/Mini_Project5/main/cars.csv'
    df = load_data(data_path)
    try:
        data_visual(df)
    except Exception as e:
        assert False, f"data_visual function raised an exception: {e}"
