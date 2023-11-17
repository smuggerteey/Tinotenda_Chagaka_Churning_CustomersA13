# Customer Churn Prediction

This project focuses on predicting customer churn, which refers to the phenomenon where customers discontinue their relationship with a business. By utilizing historical customer data and machine learning techniques, we aim to build a predictive model that can identify customers who are likely to churn. This, in turn, enables businesses to take proactive measures to retain those customers and improve overall customer retention rates.

## Dataset

The dataset used for this project contains customer information including demographics, usage patterns, and churn status. It consists of the following columns:

| Column Name    | Data Type | Description                                                  |
|----------------|-----------|--------------------------------------------------------------|
| customerID     | String    | Unique identifier for each customer                           |
| gender         | String    | Customer's gender                                            |
| SeniorCitizen  | Boolean   | Whether the customer is a senior citizen (1) or not (0)       |
| Partner        | Boolean   | Whether the customer has a partner (1) or not (0)             |
| Dependents     | Boolean   | Whether the customer has dependents (1) or not (0)            |
| tenure         | Integer   | Number of months the customer has been with the company       |
| PhoneService   | String    | Whether the customer has phone service (Yes) or not (No)      |
| MultipleLines  | Boolean   | Whether the customer has multiple phone lines (1) or not (0)   |
| InternetService| String    | Type of internet service the customer has (DSL, Fiber optic)  |
| OnlineSecurity | Boolean   | Whether the customer has online security (1) or not (0)       |
| OnlineBackup   | Boolean   | Whether the customer has online backup (1) or not (0)         |
| DeviceProtection| Boolean  | Whether the customer has device protection (1) or not (0)     |
| TechSupport    | Boolean   | Whether the customer has technical support (1) or not (0)     |
| StreamingTV    | Boolean   | Whether the customer has streaming TV (1) or not (0)          |
| StreamingMovies| Boolean   | Whether the customer has streaming movies (1) or not (0)      |
| Contract       | String    | Type of contract the customer has (Month-to-month, One year, Two year) |
| PaperlessBilling| Boolean  | Whether the customer uses paperless billing (1) or not (0)    |
| PaymentMethod  | String    | Customer's payment method (Electronic check, Mailed check, Bank transfer (automatic)) |
| MonthlyCharges | Float     | Customer's monthly charges                                   |
| TotalCharges   | Float     | Customer's total charges                                     |
| Churn          | Boolean   | Whether the customer churned (1) or not (0)                   |

## Model Training and Evaluation

The churn prediction model is trained using a supervised deep learning algorithm called a Multi-Layer Perceptron model, implemented using the Functional API. To assess the model's performance, the dataset is split into training and testing sets. Evaluation metrics such as accuracy and training/validation loss are computed to measure the effectiveness of the model in predicting churn.

## Results

The trained model achieves an accuracy of 81% on the test set, indicating its ability to correctly predict customer churn. However, further analysis is required to identify patterns and factors contributing to churn and to develop targeted strategies for customer retention.

## Future Enhancements

- **Feature Engineering**: Explore additional customer features or derive new features that may improve prediction accuracy.
- **Model Optimization**: Experiment with different machine learning algorithms or hyperparameter tuning techniques to optimize the model's performance.
- **Real-time Prediction**: Develop a system capable of making churn predictions in real-time based on streaming customer data.
- **Interpretability**: Utilize techniques like feature importance analysis or SHAP values to gain insights into the factors driving customer churn.

## Contributions

Contributions to this project are welcome. If you encounter any issues or have suggestions for improvement, please open an issue or submit a pull request.

For more information and a detailed explanation of the project, please refer to the video [here](https://youtu.be/wv_U9vnM7TM).

https://youtu.be/wv_U9vnM7TM?si=N3uK0aWxUEWLVB6c



