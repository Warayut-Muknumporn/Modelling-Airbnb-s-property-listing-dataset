# Modelling-Airbnb-s-property-listing-dataset
Build a framework to systematically train, tune, and evaluate models on several tasks that are tackled by the Airbnb team

Airbnb Property Price Prediction Model

Airbnb Listing project, in which you will develop a multitude of  classification & regression models and compare their performance across different use cases.  The user will load the Airbnb dataset which contains both numerical & categorical data and perform cleaning transformations on this data. You will address the following:

Predict the tariff of each listing based on a multitude of features (Regression) 

Predict distinct Airbnb categories (entire place, apartment, etc.) (Classification)
 
Both tasks involve training multiple ML models and saving model metrics, such as precision, rmse, etc. The models are further optimised by hyper parameter tuning. The best model is saved as a joblib file along with its hyperparameters in a json format. 


# Project Description
Airbnb hosts millions of listings on their website. Sometimes it is difficult to decide what range of nightly price to set for your property but also what features and descriptions to use for the most success. On the flip side, as a consumer, it can be difficult to decipher what properties are listed at a fair price in comparison to the history of previous listing prices. Therefore, it is useful to know which features/traits are most influential for the price per night for both hosting/staying.
Using web-scraped data on Airbnb of 1000 properties, generate simple regression models and a neural network to best predict the price per night based on quantitative features that Airbnb provides. 

In this document, the discussed project is the Airbnb Listing project, in which you will develop a multitude of  classification & regression models and compare their performance across different use cases.  The user will load the Airbnb dataset which contains both numerical & categorical data and perform cleaning transformations on this data. You will address the following:

Predict the tariff of each listing based on a multitude of features (Regression) 
Predict distinct Airbnb categories (entire place, apartment, etc.) (Classification)
 
Both tasks involve training multiple ML models and saving model metrics, such as precision, rmse, etc. The models are further optimised by hyper parameter tuning. The best model is saved as a joblib file along with its hyperparameters in a json format. 

- Processed and cleaned dataset using Pandas to improve data quality.
- Visually analysed the dataset to understand it better.
- Performed feature selection to understand different features affecting the target columns.
- Trained, compared and evaluated machine learning models (Random Forest, Linear/Logistic Regression, XGBoost etc) for classification (determining different Airbnb categories) & regression (predicting tariff) use cases.
- Performed hyperparameter tuning and cross validation to optimise the results for particular metrics, such as precision in classification. 



*skills used: sci-kit-learn, numpy, pandas, matplolib, PyTorch, seaborn,

The tabular dataset has the following columns:

ID: Unique identifier for the listing

Category: The category of the listing

Title: The title of the listing

Description: The description of the listing

Amenities: The available amenities of the listing

Location: The location of the listing

guests: The number of guests that can be accommodated in the listing

beds: The number of available beds in the listing

bathrooms: The number of bathrooms in the listing

Price_Night: The price per night of the listing

Cleanliness_rate: The cleanliness rating of the listing

Accuracy_rate: How accurate the description of the listing is, as reported by previous guests

Location_rate: The rating of the location of the listing

Check-in_rate: The rating of the check-in process given by the host

Value_rate: The rating of value given by the host

amenities_count: The number of amenities in the listing

URL: The URL of the listing

bedrooms: The number of bedrooms in the listing

## This project was part of AiCore data science specialisation programme.
I document my progress and challenges that I faced throughout this project, as well as the skills and techniques learnt/utilised. 

## Milestone 1 & 2: Repo initialisation and Data Collection
## Milestone 3: Data Preparation

In this milestone, I have observed and processed the tabular data into a format that can be used to train/test models.
All empty cells were dropped. Made sure that the descriptions are of an appropriate string format. Created a tuple that contains the features and labels. Images were also processed in the prepare_image_class.py file.

Running the 'main_airbnb_data_processing.py' file, one can import the tabular_data_class.py and prepare_image_class.py to prepare the dataset into a format appropriate for machine learning for the next steps.

The final csv file is clean_tabular_data.csv,  and load_airbnb_data function will return a tuple in the features,labels format. 


## Milestone 4: Create a regression model

In this milestone, I have set up a modelling_class.py script that contains the steps to create a regression model. Namely, using the SGD regressor module. In this module I have learnt what machine learning model types there are and why some are more appropriate for analysis than other. 
I have designed my own hyperparameter tuning function but also used the scikit-learn module (GridSearchCV). I used the K-Fold Validation to see if the differences seen between the first and second best models are statistically signficant. I have beaten the base linear regression by tuning for hyperparameters.

## Milestone 5: Create a classification model

Much like the previous milestones, I implemented different classification models such as random forests, gradient boosting and decision trees to see if I can beat the baseline classification model. 

## Milestone 6: Create a configurable neural network

Here I learnt about neural networks. I used a new tool called PyTorch which allows me to create objects that hold tensor gradient values. In order to train my model, I had to process the data into a custom PyTorch dataset, which is then loaded into the model using DataLoader. Then finally, these will go through a training loop that trains the model based on training neural network functions. For my first model, I use a basic Linear regression model with 2 layers and a ReLU activation function. I tuned the model using a variety of parameters configuring learning rates and number of hidden layers.

## Describe Neural network model
This code is a machine learning script in Python that is used to train a model to predict the nightly price of Airbnb listings based on certain features. 

The script starts by importing several libraries that are used throughout the code, including matplotlib, numpy, pandas, and PyTorch. 

Next, it defines several functions that are used to clean and preprocess the data, including: "remove_rows_with_missing_ratings", "combine_description_strings", and "set_default_feature_values". All of these functions are called in the "clean_tabular_data function" to clean the data and preprocesses them for subsequent steps. The load_airbnb function is used to load the data and return the relevant features and labels in a tuple format. 

 The AirbnbNightlyPriceDataset class is a PyTorch dataset class that is used to convert the data into a format that can be used to train the model.

 The FullyConnectedNet class represents a fully connected neural network model with three hidden layers and one output layer. The input size is determined by the number of features in the data, and the output size is determined by the number of classes in the labels. The hidden sizes are determined by the number of neurons in each hidden layer. The forward function defines the forward pass of the model, in which the input data is passed through the fully connected layers and passed through an activation function (ReLU) before the final prediction is made.

The train function is used to train the model using the given data and hyperparameters. It takes the following arguments:

  model: the model to be trained
  dataset: a PyTorch dataset object that contains the training data
  optimizer: an optimizer object that is used to update the model's parameters during training
  loss_fn: a loss function that is used to calculate the difference between the model's predictions and the true labels
  _epochs: the number of training epochs to run
  batch_size: the number of samples to include in each mini-batch

The function first creates a PyTorch data loader object from the dataset, using the batch size as the number of samples per batch. It then iterates over the number of epochs, and within each epoch it iterates over the data loader object. For each batch of data, the function retrieves the input features and labels, feeds them to the model to make a prediction, and calculates the loss between the prediction and the true labels. It then performs a backward pass to calculate the gradients of the loss with respect to the model's parameters, and updates the model's parameters using the optimizer object. Finally, it returns the trained model.

Finally, the test function is used to evaluate the performance of the trained model on a separate test set.

![2](https://github.com/Warayut-Muknumporn/Modelling-Airbnb-s-property-listing-dataset/assets/116235617/66bc9260-8717-433f-95a5-48a35827b404)
![1](https://github.com/Warayut-Muknumporn/Modelling-Airbnb-s-property-listing-dataset/assets/116235617/d87033a4-b21f-44ca-8999-bca4c80c16ca)
w![1PNG](https://github.com/Warayut-Muknumporn/Modelling-Airbnb-s-property-listing-dataset/assets/116235617/b04ebc8a-f620-4675-83b9-802be14c5f0b)
