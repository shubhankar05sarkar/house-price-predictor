# House Price Predictor

A web-based House Price Prediction Dashboard developed using Flask and Scikit-learn that predicts the estimated price of a residential property using a Linear Regression model. The application uses housing features such as overall quality, living area, garage capacity, basement area, number of bedrooms, and year built to generate accurate price predictions.

---

## Project Overview

This project implements a Machine Learning-based house price prediction system using the Ames Housing Dataset from Kaggle. A Linear Regression model was trained on carefully selected housing features after preprocessing the dataset to estimate property prices accurately.

The application was developed using Python and Flask and features a responsive and user-friendly interface built with HTML, CSS, and Bootstrap.

---

## Features

* Predict house prices using Linear Regression
* Estimate prices based on important housing features
* User-friendly web interface for entering property details
* Display estimated house price instantly
* Trained using the Ames Housing Dataset from Kaggle
* Model performance evaluated using the R² Score
* Responsive and modern user interface

---

## Technologies Used

* Python
* Flask
* Scikit-learn
* Pandas
* NumPy
* Joblib
* HTML5
* CSS3
* Bootstrap 5

---

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/House-Price-Predictor.git
cd House-Price-Predictor
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Train the Machine Learning Model

```bash
python train_model.py
```

This step preprocesses the dataset, trains the Linear Regression model, evaluates its performance, and saves the trained model for prediction.

### 6. Run the Application

```bash
python app.py
```

### 7. Open in Browser

```text
http://127.0.0.1:5000
```

---

## Machine Learning Pipeline

### Dataset

The model is trained using the **Ames Housing Dataset** obtained from Kaggle, which contains residential housing information and corresponding sale prices.

### Data Preprocessing

The following preprocessing steps were performed before training the model:

* Selected relevant housing features
* Handled missing values using mean imputation
* Split the dataset into training and testing sets using an 80:20 ratio

### Model Training

A **Linear Regression** model was trained using the selected housing features to predict house prices.

### Model Evaluation

The model performance was evaluated using the **R² Score**, achieving an accuracy of approximately **0.80**, indicating that the model explains around 80% of the variance in house prices.

---

## Input Features

The prediction model uses the following property features:

| Feature         | Description                                      |
| --------------- | ------------------------------------------------ |
| Overall Quality | Overall material and finish quality of the house |
| Living Area     | Above-ground living area (square feet)           |
| Garage Capacity | Number of cars the garage can accommodate        |
| Garage Area     | Garage size (square feet)                        |
| Basement Area   | Total basement area (square feet)                |
| Full Bathrooms  | Number of full bathrooms                         |
| Bedrooms        | Number of bedrooms above ground                  |
| Year Built      | Construction year of the property                |

---

## **Author**

Created with ❤️ by **Shubhankar Sarkar** <br>
[GitHub Profile](https://github.com/shubhankar05sarkar)
