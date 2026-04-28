# solar-energy-predictor
🌞 Solar Energy Prediction & Performance Analysis System

📌 Overview
This project presents a machine learning-based system that predicts solar energy generation using environmental parameters and analyzes system performance by comparing predicted and actual energy output.
Unlike traditional systems that only show past or current data, this system provides expected energy estimation and helps identify inefficiencies in solar panel performance.

🎯 Problem Statement
Solar energy generation depends heavily on environmental factors such as irradiance and temperature. Existing systems:
Show only actual energy output
Do not predict expected generation
Cannot detect performance loss
👉 This creates difficulty in:
Energy planning
Performance monitoring
Fault detection

💡 Proposed Solution
This system:
Predicts expected solar energy output using a machine learning model
Compares it with actual energy
Calculates deviation and performance status
👉 This helps users understand:
Whether the system is working efficiently
If there is any energy loss or inefficiency

⚙️ Features
🔮 1. Energy Prediction
Uses Linear Regression model
Inputs:
GHI (Global Horizontal Irradiance)
DNI (Direct Normal Irradiance)
DHI (Diffuse Horizontal Irradiance)
Temperature
Hour

📊 2. Performance Analysis (Core Feature ⭐)
Compares:
Predicted Energy vs Actual Energy
Calculates:
Deviation
Percentage Error

🚦 3. Smart Performance Indicator:
🟢 Optimal Performance
🟡 Moderate Deviation
🔴 Poor Performance

⚠️ 4. Deviation-Based Insights
Detects possible inefficiencies such as:
Panel dirt
Shading
System losses
Environmental variations

📈 5. Visualization
Graphs for Predicted vs Actual Energy
Helps in understanding trends and performance

🌐 6. Web Interface
Built using Flask
User-friendly input form
Instant prediction results

🛠️ Tech Stack
Programming Language
Python:
Libraries:
NumPy
Pandas
Scikit-learn
Matplotlib

Framework:
Flask
Frontend
HTML / CSS

🧠 Machine Learning Concepts Used:
Supervised Learning
Linear Regression
Train-Test Split
Model Evaluation:
Mean Absolute Error (MAE)
R² Score

🔄 System Workflow
User Input → Flask Backend → ML Model → Prediction → Comparison → Output Display
User enters environmental parameters
Model predicts expected energy
System compares with actual energy (if provided)
Displays:
Predicted Energy
Deviation
Performance Status

📊 Example Output
Input:
GHI = 265
DNI = 206
DHI = 173
Temperature = 9
Hour = 22
Actual Energy = 176
Output:
Predicted Energy = 220.95
Deviation = 44.95 (25.54%)
Status = Poor Performance

⚠️ Limitations
Uses Linear Regression (assumes linear relationships)
Does not include all real-world factors such as:
Humidity
Dust
Panel tilt
Cloud dynamics
Model accuracy depends on dataset quality

👉 High deviation may indicate:
System inefficiency
OR
Model limitations

🚀 Future Scope
Integration with real-time IoT sensors
Use of advanced models:
Random Forest
Gradient Boosting
Neural Networks
Integration with weather APIs
Deployment as a scalable web/mobile application
Smart recommendations for maintenance

🌍 Applications
Solar Power Plants
Rooftop Solar Systems
Industrial Energy Management
Performance Monitoring & Fault Detection

🧾 Conclusion
This project demonstrates how machine learning can be used not only to predict solar energy but also to analyze system performance.
By comparing expected and actual output, the system provides meaningful insights that help in:
Improving efficiency
Detecting issues
Supporting better energy planning

👩‍💻 Authors
Tanishka Takawane
Srivardhani Vavilasetty

📜 License
This project is for educational purposes. You can add an MIT License if you want to make it open-source.

⭐ Final Note
This is not just a prediction model — it is a decision-support system for solar performance analysi
