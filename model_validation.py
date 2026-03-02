import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error

mel_data = pd.read_csv('melb_data.csv')


filtered_mel_data = mel_data.dropna(axis=0)

selected_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']

X = filtered_mel_data[selected_features]

y = filtered_mel_data.Price

mel_model = DecisionTreeRegressor(random_state=1)

mel_model.fit(X, y)


print(mel_model.predict(X.head()))



predicted_home_prices = mel_model.predict(X)

mean_absolute_error(y, predicted_home_prices)


err = mean_absolute_error(y, predicted_home_prices)

print(err)