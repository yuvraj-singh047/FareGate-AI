# ✈️ FareGate - Flight Fare Prediction

An end-to-end Machine Learning web application that predicts the price of domestic flights in India based on travel details such as airline, source, destination, departure time, arrival time, number of stops, and more.

Built using **Python**, **Scikit-learn**, **XGBoost**, and **Flask**, with a modern airline-inspired UI.

---

## 📸 Homepage

<p align="center">
  <img src="screenshots/home.png" alt="FareGate Homepage" width="100%">
</p>

---

## 🚀 Features

- ✈️ Predict domestic flight fares instantly
- 🎨 Modern boarding-pass inspired UI
- 🤖 XGBoost Regression model
- ⚡ Fast Flask backend
- 📊 Data preprocessing using Scikit-learn Pipeline
- 🧹 Feature engineering from date, time, and duration
- 📱 Responsive interface
- 🎯 Trained using GridSearchCV for hyperparameter tuning

---

## 🛠 Tech Stack

### Machine Learning
- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost

### Backend
- Flask
- Pickle

### Frontend
- HTML5
- CSS3
- JavaScript

---

## 📂 Project Structure

```text
Flight-Fare-Prediction/
│
├── app.py
├── requirements.txt
├── README.md
│
├── models/
│   ├── model.pkl
│   └── preprocessor.pkl
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   └── index.html
│
├── screenshots/
│   └── homepage.png
│
└── notebook/
    └── notebook.ipynb
```

---

## 📊 Dataset

The model was trained on the **Flight Fare Prediction** dataset from Kaggle.

The dataset contains flight booking information including:

- Airline
- Source
- Destination
- Journey Date
- Departure Time
- Arrival Time
- Duration
- Total Stops
- Additional Information
- Ticket Price (Target)

---

## ⚙️ Feature Engineering

The following preprocessing steps were performed:

- Removed duplicate records
- Extracted:
  - Journey Day
  - Journey Month
  - Journey Year
  - Departure Hour
  - Departure Minute
  - Arrival Hour
  - Arrival Minute
  - Duration Hour
  - Duration Minute
- Encoded categorical features
- Standardized numerical features
- Built preprocessing pipeline using `ColumnTransformer`

---

## 🤖 Model Training

The following regression models were evaluated:

- Linear Regression
- Ridge Regression
- Lasso Regression
- Decision Tree Regressor
- Random Forest Regressor
- KNN Regressor
- XGBoost Regressor

After hyperparameter tuning using **GridSearchCV**, **XGBoost Regressor** achieved the best performance.

### Model Performance

| Metric | Score |
|---------|-------|
| R² Score | **92.64%** |

---

## 💻 Installation

Clone the repository

```bash
git clone https://github.com/<YOUR_USERNAME>/Flight-Fare-Prediction.git
```

Move into the project directory

```bash
cd Flight-Fare-Prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Flask application

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000/
```

---

## 📷 Application Workflow

1. Select Source Airport
2. Select Destination Airport
3. Choose Airline
4. Enter Journey Date
5. Enter Departure Time
6. Enter Arrival Time
7. Select Total Stops
8. Select Additional Information
9. Click **Predict Fare**
10. View the estimated ticket price

---

## 🎯 Future Improvements

- Live airline fare API integration
- Flight duration auto-calculation
- Currency conversion
- Dark mode
- Airline logos
- Docker deployment
- Cloud deployment (Render/AWS)

---

## 👨‍💻 Author

**Yuvraj Singh**

- GitHub: https://github.com/<YOUR_USERNAME>
- LinkedIn: *(Add your LinkedIn profile here)*

---

## ⭐ If you found this project helpful

Please consider giving this repository a **star** ⭐
