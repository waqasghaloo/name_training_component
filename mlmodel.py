import xgboost as xgb
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split

california_housing = fetch_california_housing()

# Retrieve data from fetch_california_housing function
X = california_housing.data
y = california_housing.target

print(f"Shape of X in Input data is {X.shape}")
print(f"Shape of Y in Input data is {y.shape}")

# Step # 1: Spliting data into train and test split
X_train,X_test,y_train,y_test= train_test_split(X,y,test_size=0.20)

# Step # 2: Converting splited data to DMatrix.
dtrain = xgb.DMatrix(data = X_train, label = y_train)
dtest  = xgb.DMatrix(data = X_test , label = y_test )

params = {
    'n_estimators': 100,
    'verbosity': 1,

    # 'eval_metric': 'mae',
    'verbosity' : 2
}


# Step #3: Compile XGBoost Regresssor model with parameters, there are two
# ways to pass parameters
# Way#1: Pass directly to model
# Way#2: Pass as dictionary and use **before dict name while passing to model
# ** will make model to interpret keys of dict as parameters and value as value of parameter
# model = xgb.XGBRegressor(**params)

# the compile() method is used to specify the optimizer, loss function, 
# and evaluation metrics for the model. This is followed by the fit() method, 
# which is used to train the model on the data and optimize the model parameters.

# model = xgb.XGBRegressor(max_depth = 3, learning_rate = 0.1, n_estimators =100, objective='reg:squarederror', booster='gbtree')

model = xgb.XGBRegressor(**params)

model.fit(X_train, y_train, eval_set=[(X_test, y_test)], eval_metric='rmse', early_stopping_rounds=10)



print(model.base_score)


