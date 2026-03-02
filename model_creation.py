import pandas as pd
from sklearn.tree import DecisionTreeRegressor



mel_data = pd.read_csv('melb_data.csv')

print(mel_data.head())
print(mel_data.head().Price)
print(mel_data.columns)



y = mel_data.Price

selected_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']

X = mel_data[selected_features]

X.describe()

X.head()

print(X.describe())

print(X.head())
#on peut utiliser usecols comme ceci pour préciser les colonnes à prendre en compte
#mel_data = pd.read_csv('melb_data.csv', usecols=['Rooms', 'Distance', 'Landsize', 'BuildingArea', 'Price'])



melbourne_model = DecisionTreeRegressor(random_state=1)


melbourne_model.fit(X, y)


print("Making predictions for the following 5 houses:")
print(X.head())
print("The predictions are")
print(melbourne_model.predict(X.head()))





















