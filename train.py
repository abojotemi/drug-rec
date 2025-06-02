from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import pickle

X_train =pd.read_csv('X_train (1).csv', encoding='ISO-8859-1', index_col=False )
X_test =pd.read_csv('X_test (3).csv', encoding='ISO-8859-1', index_col=False )
y_train =pd.read_csv('y_train (2).csv', encoding='ISO-8859-1', index_col=False )
y_test =pd.read_csv('y_test (4).csv', encoding='ISO-8859-1', index_col=False )

model = RandomForestClassifier()
model.fit(X_train,y_train)

with open('Recommendation_model.sav', 'wb') as file:
  pickle.dump(model, file)