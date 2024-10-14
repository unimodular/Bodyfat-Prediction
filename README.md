# Bodyfat Prediction

### Shuo Li, Yunze Wang, Xinrui Zhong

This repository is used for STAT 628 module_2 Body Fat Study Assignment. All of our works are included in this repository.


## Overview
This project aims to develop a predictive model for estimating body fat percentage using various physical measurements. The dataset used in this project is **BodyFat.csv**, which contains data on 252 male individuals, including their body fat percentages and body measurements.

## Requirements
To run the code, you will need the following libraries installed in your environment. The code is in the 

```python
import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, GridSearchCV, KFold, cross_val_score
from sklearn.metrics import accuracy_score, mean_squared_error
from sklearn.inspection import permutation_importance
from sklearn.impute import KNNImputer
from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor, plot_tree, export_text

```



You can install these dependencies using `pip`:

```bash
pip install numpy pandas statsmodels matplotlib seaborn scikit-learn
```

## How to Use

1. **Open the `code` folder** and download the notebook file named **`Fat_prediction1.1.ipynb`**.
2. Place this file in the same directory as the **`BodyFat.csv`** dataset, located in the `data` folder.
3. After setting up the environment with the required libraries (as listed above), you can run the notebook and execute the model analysis.

Once your environment is properly configured, you will be able to run the code and reproduce the results.

