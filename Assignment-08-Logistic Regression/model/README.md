# Model Information

## 📦 Model Name
Diabetes Prediction Model

---

## 📌 Description
This file contains the trained Logistic Regression Machine Learning model used for predicting diabetes risk based on patient health parameters.

The model was trained using the Diabetes Prediction Dataset and saved using Python's `pickle` library for deployment in a Streamlit web application.

---

## 📂 File Included
- `diabetes_model.pkl`

---

## 🛠️ Technologies Used
- Python
- Scikit-learn
- Pickle
- Logistic Regression

---

## ⚙️ Model Usage
The saved model is loaded in the Streamlit application using:

```python
pickle.load(open("model/diabetes_model.pkl", "rb"))
```

The model predicts:
- `0` → No Diabetes
- `1` → Diabetes Risk

---

## 📈 Purpose
This model is used for:
- Diabetes Risk Prediction
- Machine Learning Deployment
- Healthcare Classification Tasks

---

## ⚠️ Note
This model file is used only for educational and learning purposes.
