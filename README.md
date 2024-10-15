# Credit Card Fraud Detection

## 📈 Overview
Welcome to the Credit Card Fraud Detection project! This repository contains a comprehensive machine-learning workflow to detect fraudulent credit card transactions using advanced techniques and methodologies.

## 🛠️ Features

### ◆ Data Exploration & Preprocessing
- Loaded and inspected the Credit Card Fraud Detection dataset from Kaggle.
- Handled data scaling using StandardScaler.
- Addressed class imbalance through undersampling and oversampling techniques.

### ◆ Model Training & Evaluation
- Implemented various machine learning algorithms:
  - Logistic Regression
  - Decision Tree Classifier
- Evaluated models using metrics such as Accuracy, Precision, Recall, and F1-Score.
- Fine-tuned models to enhance performance and reliability.

### ◆ Model Persistence
- Saved the trained model using joblib for future use and deployment.

### ◆ Deployment Prototype
- Developed a basic user interface using Streamlit (currently facing installation issues).

## 📊 Dataset
The project utilizes the Credit Card Fraud Detection dataset, which includes transactions made by credit cards in September 2013 by European cardholders. This dataset presents transactions that occurred in two days, where we have 492 frauds out of 284,807 transactions. The dataset is highly unbalanced, the positive class (frauds) accounting for 0.172% of all transactions.

## 📚 Project Structure
- `credit_card_model.pkl`: Serialized machine learning model.
- `Credit_Card_Fraud_Detection.ipynb`: Jupyter Notebook containing the full project workflow.
- `README.md`: Project documentation.

## 💾 Installation

### Clone the Repository
```bash
git clone https://github.com/yourusername/credit-card-fraud-detection.git
cd credit-card-fraud-detection
```


## Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```
## Install Dependencies

```bash
pip install -r requirements.txt
```
Note: If you encounter issues installing Streamlit, ensure your internet connection is stable or try again later.

## 🚀 Usage

Jupyter Notebook

Open Credit_Card_Fraud_Detection.ipynb in Jupyter Notebook to explore the project workflow, from data preprocessing to model evaluation.
Model Deployment (Streamlit)

Note: Streamlit installation faced connectivity issues. Once resolved, you can run the app as follows:

```bash

streamlit run creditcheck.py
```

The app provides a user-friendly interface to input transaction details and predict fraudulence.

## 🔍 Evaluation Metrics

Accuracy: Measures the proportion of correct predictions.

Precision: Indicates the accuracy of positive predictions.

Recall: Measures the ability of the model to find all relevant cases.

F1-Score: Harmonic mean of Precision and Recall.

## 🤝 Acknowledgements

This project was inspired and guided by KNOWLEDGE DOCTOR on YouTube. Their insightful tutorials and walkthroughs were instrumental in shaping this project.

## Contact
For any further questions or project collaborations, feel free to reach out via GitHub.
