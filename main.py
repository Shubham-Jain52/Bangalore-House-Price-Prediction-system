import pandas as pd
import pickle
from flask import Flask, render_template, request, jsonify

# Load the data and model
data = pd.read_csv('C:/Users/KIIT0001/OneDrive/Desktop/DataScience/practice projects/Banglore house price prediction/cleaned_Dataset.csv')
model = pickle.load(open('C:/Users/KIIT0001/OneDrive/Desktop/DataScience/practice projects/Banglore house price prediction/ridgeModel.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def index():
    locations = sorted(data['location'].unique())
    return render_template('index.html', locations=locations)

@app.route('/predict', methods=['POST'])
def prediction():
    # Retrieve input values from the form
    location = request.form.get('Location')
    bhk = int(request.form.get('BHK'))
    bathrooms = int(request.form.get('bathrooms'))
    sqft = float(request.form.get('sqft'))
    print(location,bhk,bathrooms,sqft)
    # Prepare the input for the model
    input_data = pd.DataFrame([[location, sqft, bathrooms, bhk]], 
                              columns=['location', 'total_sqft', 'bath', 'BHK'])
    print(input_data)
    
    # Make prediction
    prediction = model.predict(input_data)[0]
    result = f"The predicted price is  {round(prediction, 2)} Lakh rupees"
    
    # Return the result as JSON
    return jsonify({'prediction': result})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
