import joblib
import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import roc_auc_score

dataframe = pd.read_csv("~/Documents/datasets/credit_score_classification/transformed_train.csv")

X = dataframe.drop(columns=['Credit_Score'])
y = dataframe['Credit_Score']

numerical_features = dataframe.columns[dataframe.dtypes == 'float']
categorical_features = dataframe.columns[dataframe.dtypes == 'object']

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_features),
        ('cat', OneHotEncoder(), categorical_features)
    ]
)

pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', XGBClassifier(colsample_bytree = 0.606,
                                     gamma = 0.256,
                                     learning_rate = 0.075,
                                     max_depth = 10,
                                     min_child_weight = 7,
                                     n_estimators = 869,
                                     reg_alpha = 0.94,
                                     reg_lambda = 1.397,
                                     subsample = 0.807))
])

X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.2,
                                                    shuffle= True,
                                                    stratify=y,
                                                    random_state=42)

pipeline.fit(X_train, y_train)

joblib.dump(pipeline, 'models/best_model.pkl')

