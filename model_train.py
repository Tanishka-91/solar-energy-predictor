import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import pickle
import matplotlib.pyplot as plt
import os

df = pd.read_csv("solar_50k.csv")

features = ['GHI', 'DNI', 'DHI', 'Temp', 'hour']
X = df[features]
y = df['Energy']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("MAE:", mae)
print("R2 Score:", r2)

model_data = {
    "model": model,
    "features": features,
    "mae": mae,
    "r2": r2
}

pickle.dump(model_data, open("model.pkl", "wb"))
print("Model and metadata saved successfully")

comparison = pd.DataFrame({
    'Actual': y_test.values[:10],
    'Predicted': y_pred[:10]
})

print("\nSample Predictions:")
print(comparison)

safe_y_test = y_test.replace(0, 1e-6)

error_percent = abs((safe_y_test - y_pred) / safe_y_test) * 100

print("\nPercentage Error (first 10):")
print(error_percent[:10])

os.makedirs("static", exist_ok=True)

plt.figure()
plt.plot(y_test.values[:50], label="Actual")
plt.plot(y_pred[:50], label="Predicted")
plt.legend()
plt.title("Actual vs Predicted Energy")

plt.savefig("static/graph.png")
plt.close()

print("Graph saved in static/graph.png")