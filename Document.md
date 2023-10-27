# Document: Data Manipulation Tasks 
## 1. Data Preview

Before diving into any data manipulation, the script first previews the dataset. This allows us to understand the structure of the data.

```python
df_preview = pd.read_csv(path, sep=';')
df_preview.head()
df_preview.info()
```

## 2. Loading Data Function

A function named `load_data` is defined to streamline the process of loading datasets from a given path.

```python
def load_data(data_path):
    return pd.read_csv(data_path, sep=';')
```

## 3. Data Summary Function

The `data_summary` function provides a concise summary of the dataset, displaying statistics like mean, median, standard deviation, and more.

```python
def data_summary(data):
    return data.describe()
```

## 4. Data Visualization Function

Visualizing data helps in understanding patterns and outliers. The `data_visual` function creates a boxplot showing the weight distribution of cars based on their origin.

```python
def data_visual(data):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        sns.set_theme(style="ticks", palette="pastel")
        sns.boxplot(x='Origin', y='Weight', palette="Blues", data=data)
        plt.show()
```

## 5. Generating Random Data

Random datasets can be useful for simulation or testing purposes. Here, a random dataset is generated with the same number of rows as the original dataset.

```python
num_rows = len(my_df)
random_data = {
    'Random_Value1': np.random.randint(1, 101, num_rows),
    'Random_Value2': np.random.rand(num_rows) * 100,
    'Random_Category': np.random.choice(['A', 'B', 'C', 'D'], num_rows)
}
random_df = pd.DataFrame(random_data)
```

## 6. Merging Datasets

Both the original dataset and the random dataset are merged to create a combined dataset.

```python
merged_df = pd.concat([my_df, random_df], axis=1)
```
