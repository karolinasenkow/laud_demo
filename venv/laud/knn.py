import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_validate
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier

knn_df = pd.read_csv("laud/dim_df.csv")

data = knn_df.iloc[:,-(len(knn_df.columns) - 2):].values
data = StandardScaler().fit_transform(data)
target = knn_df["cure_status"].values
train_data, test_data, train_target, test_target = train_test_split(data, target, test_size=0.3, random_state=216)

params_to_try = {"n_neighbors": range(1, 30)}
knn_search = GridSearchCV(estimator = KNeighborsClassifier(), param_grid = params_to_try, cv = 10)
knn_search.fit(train_data, train_target)

vec = pd.read_csv("laud/static/uploads/ML_sample_input.csv")
v = vec.iloc[:,-(len(vec.columns)-1):].values.tolist()
predicted = knn_search.predict(v)


f = open("laud/ML_knn_outfile.txt", "w+")
f.write(str(knn_search.best_params_))
f.write("\n")
f.write("Accuracy on training data: " + str(knn_search.score(train_data, train_target)))
f.write("\n")
f.write("Accuracy on testing data: " + str(knn_search.score(test_data, test_target)))
f.write("\n")
f.write("Predicted cure status: " + str(predicted))
f.close()
