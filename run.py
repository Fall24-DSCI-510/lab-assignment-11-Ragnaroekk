# Solution code for the Iris Dataset Homework (run.py)

import pandas as pd
from scipy.stats import zscore

# Question 1: Pre-process the data
def preprocess_data(input_filename) -> pd.DataFrame:
    '''Output : A DataFrame without samples where SepalLengthCm or SepalWidthCm has a z-score <-2 or >2'''
    # research from https://stackoverflow.com/questions/18172851/deleting-dataframe-row-in-pandas-based-on-column-value
    columns = ["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm", "Species"]
    df = pd.read_csv(input_filename, names=columns)
    
    # get the z-scores
    df['SepalLengthCm_z'] = zscore(df['SepalLengthCm'])
    df['SepalWidthCm_z'] = zscore(df['SepalWidthCm'])   
    
    # delete each row where the new value is outside the range of -2 to 2
    df = df[df.SepalLengthCm_z < 2]
    df = df[df.SepalLengthCm_z > (-2)]
    df = df[df.SepalWidthCm_z < 2]
    df = df[df.SepalWidthCm_z > (-2)]

    # create an ID column with range starting at 1
    df["ID"] = range(1, len(df) + 1)
    return df

# Question 2: Descriptive Statistics Functions
def species_count(data) -> dict:
    data = preprocess_data("iris.data")
    return dict(data["Species"].value_counts())

def average_sepal_length(data) -> float:
    data = preprocess_data("iris.data")
    return round(data["SepalLengthCm"].mean(), 1)

def max_petal_width(data) -> float:
    data = preprocess_data("iris.data")
    return round(data["PetalWidthCm"].max(), 1)

def min_petal_length(data) -> float:
    data = preprocess_data("iris.data")
    return round(data["PetalLengthCm"].min(), 1)

def count_sepal_length_above_5(data) -> int:
    data = preprocess_data("iris.data")
    return len(data[data.SepalLengthCm > 5.0])

# Question 3: Analysis Functions
def count_petal_length_below_2(data) -> int:
    data = preprocess_data("iris.data")
    return len(data[data.PetalLengthCm < 2.0])

def get_sepal_width_above_3_5(data) -> list:
    data = preprocess_data("iris.data")
    result = list(data.loc[data["SepalWidthCm"] > 3.5, 'ID'])
    result.sort()
    return result

def species_count_petal_width_above_1_5(data) -> dict:
    pass

def get_virginica_petal_length_above_6(data) -> list:
    pass
    
def get_largest_sepal_width(data) -> int:
    pass

print(get_sepal_width_above_3_5("j"))