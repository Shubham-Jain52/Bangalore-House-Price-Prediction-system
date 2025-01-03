# Bangalore-House-Price-Prediction-system
This project is a web-based application that predicts house prices in Bangalore using a machine learning model. It allows users to input details such as location, square footage, number of bedrooms (BHK), and bathrooms to get an estimated price for a property.

## Features

**User-Friendly Interface:** A responsive and interactive web interface built with HTML, CSS, and Bootstrap.
**Real-Time Predictions:** Get house price predictions instantly based on user inputs.
**Machine Learning Model:** Utilizes a trained Ridge Regression model for accurate predictions.
**Dynamic Location Options:** Dropdown menu dynamically populated with real Bangalore locations from the dataset.
**Flask Backend:** Lightweight and scalable backend for handling user requests and serving predictions.

## How It Works
### Input Features:

**Location:** Select from a dropdown of Bangalore locations.
**BHK:** Enter the number of bedrooms.
**Bathrooms:** Enter the number of bathrooms.
**Square Footage:** Enter the total square footage of the property.

### Prediction:
The user submits the form, and the data is sent to the Flask server.
The server processes the input data and uses a pre-trained Ridge Regression model (stored in a pickle file) to predict the price.
The predicted price is displayed instantly on the web page.

## Tech Stack
**Frontend:**
HTML5, CSS3, Bootstrap 4.4.1
JavaScript for AJAX-based communication with the backend

**Backend:**
Flask (Python-based web framework)
Ridge Regression model (trained using Scikit-learn)

**Data:**

Cleaned dataset of Bangalore house prices - https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data

## Prerequisites:

**Python 3.6 or higher**

**Flask**

**Scikit-learn**

**Pandas**

**Numpy**

## Future Enhancements
Add more features like property age, amenities, and parking spaces for better predictions.
Implement data visualization for trends and insights.
Deploy the app on a cloud platform like Heroku or AWS.
