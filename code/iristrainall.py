label_col = 'species'
data_cols = ['petal length (cm)','petal width (cm)']
X = iris_df[data_cols].values
y = iris_df[label_col].values
# Quadratic Discriminant Analysis
qda = QuadraticDiscriminantAnalysis(store_covariance=True)
y_pred = qda.fit(X, y).predict(X)