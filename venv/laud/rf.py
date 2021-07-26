import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_validate
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier

rf_df = pd.read_csv("laud/dim_df.csv")

data = rf_df.iloc[:,-(len(rf_df.columns) - 2):].values
data = StandardScaler().fit_transform(data)
target = rf_df["cure_status"].values
train_data, test_data, train_target, test_target = train_test_split(data, target, test_size=0.3, random_state=216)

params_to_try = {"n_neighbors": range(1, 30)}

# Create the parameter grid based on the results of random search
param_grid = {'n_estimators': [10, 25], 'max_features': [5, 10], 'max_depth': [10, 50, None], 'bootstrap': [True, False]}


rf_search = GridSearchCV(estimator = RandomForestClassifier(), param_grid = param_grid, cv = 10, n_jobs = -1, verbose = 2)
rf_search.fit(train_data, train_target)

vec = pd.read_csv("laud/static/uploads/ML_sample_input.csv")
v = vec.iloc[:,-(len(vec.columns)-1):].values.tolist()
predicted = rf_search.predict(v)


f = open("laud/ML_rf_outfile.txt", "w+")
#f.write(str(rf_search.best_params_))
#f.write("\n")
f.write("Accuracy on training data: " + str(rf_search.score(train_data, train_target)))
f.write("\n")
f.write("Accuracy on testing data: " + str(rf_search.score(test_data, test_target)))
f.write("\n")
f.write("Predicted cure status: " + str(predicted))
f.close()
