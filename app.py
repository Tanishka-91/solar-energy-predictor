from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model data
model_data = pickle.load(open("model.pkl", "rb"))
model = model_data["model"]
features = model_data["features"]
mae = model_data["mae"]
r2 = model_data["r2"]

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # ---- INPUT ----
        ghi = float(request.form['ghi'])
        dni = float(request.form['dni'])
        dhi = float(request.form['dhi'])
        temp = float(request.form['temp'])
        hour = int(request.form['hour'])
        actual = request.form.get('actual')

        # ---- VALIDATION ----
        if not (0 <= ghi <= 1200):
            return render_template("index.html", prediction_text="Invalid GHI (0-1200)")

        if not (0 <= dni <= 1200):
            return render_template("index.html", prediction_text="Invalid DNI (0-1200)")

        if not (0 <= dhi <= 600):
            return render_template("index.html", prediction_text="Invalid DHI (0-600)")

        if not (-10 <= temp <= 60):
            return render_template("index.html", prediction_text="Invalid Temperature (-10 to 60°C)")

        if not (0 <= hour <= 23):
            return render_template("index.html", prediction_text="Invalid Hour (0-23)")

        # ---- PREPARE INPUT ----
        input_dict = {
            "GHI": ghi,
            "DNI": dni,
            "DHI": dhi,
            "Temp": temp,
            "hour": hour
        }

        input_data = np.array([[input_dict[f] for f in features]])

        # ---- PREDICTION ----
        prediction = model.predict(input_data)[0]
        result = f"Predicted Energy: {prediction:.2f} kWh"

        deviation_text = ""
        status_text = ""
        note = ""

        # ---- IF ACTUAL PROVIDED ----
        if actual:
            actual = float(actual)

            if actual < 0:
                return render_template("index.html", prediction_text="Actual energy cannot be negative")

            deviation = prediction - actual
            error_percent = (abs(deviation) / actual) * 100 if actual != 0 else 0
            # ⚠️ High deviation warning
            if error_percent > 100:
                note = "⚠️ Very high deviation — check input or system condition"
            else:
                note = ""
            # performance label
            if error_percent < 10:
                status = "Optimal "
            elif error_percent < 25:
                status = "Moderate "
            else:
                status = "Poor"

            deviation_text = f"Deviation: {deviation:.2f} kWh ({error_percent:.2f}%)"
            status_text = f"Performance: {status}"

        return render_template(
            "index.html",
            prediction_text=result,
            deviation_text=deviation_text,
            note_text=note,
            status_text=status_text,
            model_info=f"MAE: {mae:.2f}, R²: {r2:.2f}"
        )

    except ValueError:
        return render_template("index.html", prediction_text="Please enter valid numeric values")

    except Exception as e:
        return render_template("index.html", prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)