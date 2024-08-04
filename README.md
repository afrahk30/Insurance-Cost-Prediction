Medical Insurance Cost Prediction

Problem Statement
Insurance companies need to accurately predict the cost of health insurance for individuals to set premiums appropriately.
Traditional methods of cost prediction often rely on broad actuarial tables and historical averages, which may not account for the nuanced differences among individuals. By leveraging
machine learning techniques, insurers can predict insurance costs more accurately, tailored to individual profiles, leading to more competitive pricing and better risk management.

Steps Taken to Solve the Problem:

1. Exploratory Data Analysis (EDA)
EDA was conducted to understand the dataset better and identify the key factors influencing insurance costs.
This included:

Visualizing Distributions: Histograms and box plots were used to visualize the distribution of features such as age, BMI, and premium costs.
Identifying Outliers: Outliers were identified and handled appropriately to prevent them from skewing the model.
Exploring Correlations: Heatmaps were used to explore correlations between different variables and the target variable (insurance premium costs).

2. Hypothesis Testing
Hypothesis testing was performed to validate assumptions about the data:

Chronic Diseases Impact: Tested if the presence of chronic diseases significantly impacts insurance premiums.
Major Surgeries Impact: Tested if the number of major surgeries significantly affects premium costs.
Family History of Cancer Impact: Tested if individuals with a family history of cancer have higher premium costs. etc.

3. Machine Learning Modeling
The dataset was used to train a machine learning model to predict insurance premiums.  The steps included:

Data Preprocessing:
Outliers were treated with the IQR Method
Feature Engineering:
Some features like height and weight were highly multicorrelated so they were treated using Variance Inflation Factor.
BMI was calculated from height and weight.
Data Splitting:
The data was splitted into training data, validation data and test data.
A RandomForestRegressor was chosen as the final model for its better results and accuracy scores.
Model Training:
The training data was trained on three different models - Linear Regression, Decision Tree Regressor, Random Forest Regressor and Gradien Boosting. All the three models were tuned to find
their best parameters (Hyperparameter Tuning)
Model Selection:
Finally Random Forest Regressor was chosen as the final model for its better results and accuracy scores.
Model Evaluation:
The model's performance was evaluated using metrics such as Mean Absolute Error (MAE) ,R-squared and Adjusted R-squared.
The final model achieved Adjusted R-squared score of 0.86.


This approach was chosen due to its systematic and thorough nature, ensuring that each step from data understanding to model deployment was covered comprehensively. 
The use of EDA and hypothesis testing helped in identifying key features and validating assumptions, leading to a robust model. 

By following this approach, the resulting model is not only accurate but also interpretable and easy to use, meeting the requirements of the insurance industry for precise and 
personalized premium predictions.
