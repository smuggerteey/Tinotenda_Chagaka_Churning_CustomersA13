import streamlit as st
import numpy as np
import tensorflow as tf
import pandas as pd

# Load the trained model
model = tf.keras.models.load_model('TrainedModel.h5')

def main():
    st.title('Churn Prediction')

    # Adding user input elements
    tenure = st.number_input('Tenure:', value=1)
    online_security = st.selectbox('Online Security:', ['No', 'Yes', 'No Internet Service'])
    device_protection = st.selectbox('Device Protection:', ['No', 'Yes', 'No Internet Service'])
    tech_support = st.selectbox('Tech Support:', ['No', 'Yes', 'No Internet Service'])
    streaming_tv = st.selectbox('Streaming TV:', ['No', 'Yes', 'No Internet Service'])
    streaming_movies = st.selectbox('Streaming Movies:', ['No', 'Yes', 'No Internet Service'])
    contract = st.selectbox('Contract:', ['Month-to-Month', 'One Year', 'Two Year'])
    payment_method = st.selectbox('Payment Method:', ['Electronic Check', 'Mailed Check', 'Bank Transfer (Automatic)', 'Credit Card (Automatic)'])
    monthly_charges = st.number_input('Monthly Charges:', value=1.0)
    total_charges = st.number_input('Total Charges:', value=1.0)

    # Process user input and make predictions
    if st.button('Predict'):
        # Convert categorical variables to binary indicators
        online_security = 1 if online_security == 'No' else 0
        device_protection = 1 if device_protection == 'No Internet Service' else 0
        tech_support = 1 if tech_support == 'No' else 0
        streaming_tv = 1 if streaming_tv == 'No Internet Service' else 0
        streaming_movies = 1 if streaming_movies == 'No Internet Service' else 0
        contract= 1 if contract == 'Month-to-Month' else 0
        contract = 2 if contract == 'One Year' else 0
        contract = 3 if contract == 'Two Year' else 0
        payment_electronic_check = 1 if payment_method == 'Electronic Check' else 0

        # Prepare input array for prediction
        input_data = [
            tenure,
            online_security,
            device_protection,
            tech_support,
            streaming_tv,
            streaming_movies,
            contract,
            payment_electronic_check,
            monthly_charges,
            total_charges
        ]

        input_array = np.array(input_data).reshape(1, 10)

        # Make predictions
        predictions = model.predict(input_array)

        # Display predictions
        if predictions > 0.5:
            result = "Customer Churn Occurs"
        else:
            result = "No Churn Occurs"

        st.write('Predicted Result:', result)
        st.write('Prediction value:', (predictions))

if __name__ == '__main__':
    main()
