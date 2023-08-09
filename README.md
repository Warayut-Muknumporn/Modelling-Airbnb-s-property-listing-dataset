# Modelling-Airbnb-s-property-listing-dataset
Build a framework to systematically train, tune, and evaluate models on several tasks that are tackled by the Airbnb team

Airbnb Property Price Prediction Model

# Project Description
Airbnb hosts millions of listings on their website. Sometimes it is difficult to decide what range of nightly price to set for your property but also what features and descriptions to use for the most success. On the flip side, as a consumer, it can be difficult to decipher what properties are listed at a fair price in comparison to the history of previous listing prices. Therefore, it is useful to know which features/traits are most influential for the price per night for both hosting/staying.
Using web-scraped data on Airbnb of 1000 properties, generate simple regression models and a neural network to best predict the price per night based on quantitative features that Airbnb provides. 

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
Check-in_rate: The rating of check-in process given by the host
Value_rate: The rating of value given by the host
amenities_count: The number of amenities in the listing
url: The URL of the listing
bedrooms: The number of bedrooms in the listing
