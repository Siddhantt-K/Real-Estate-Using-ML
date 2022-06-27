
## Click below to view the Web App
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://siddhantt-k-real-estate-using-machine-learning-app-0c9hx2.streamlitapp.com)


### Demo Image

![Capture](https://user-images.githubusercontent.com/87244972/176013382-739b36cb-8de2-4f08-8283-b6973abfcf68.PNG)


## Author

- [@Siddhantt-K](https://www.github.com/Siddhantt-K)


## Table of Contents

  - [Business problem](#business-problem)
  - [Data source](#data-source)
  - [Workflow](#workflow)
  - [Tech Stack](#tech-stack)
  - [Quick glance at the results](#quick-glance-at-the-results)
  - [Deployment on streamlit](#deployment-on-streamlit)
  - [Repository structure](#repository-structure)


## Business problem

Predicting price of a Bangalore apartment.


## Data source

- [Dataset](https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data)


## Workflow

- Data Preparation : Cleaned few columns.
                     Derived few columns from existing one's (for further outlier removal process).


- Feature Engineering : Analysis of the features and found some unusual patterns.
                        Removal of outliers.
                        
- Model Building : Performed 3 algorithms on the data- 1)Linear Regression, 2)Support Vector Machine(SVM) and 3)Decision Tree
                   Saved the good performing model using Pickle.

- Evaluation of Model : R2 Score

- Production with Streamlit : Created a web app using Streamlit.


## Tech Stack

- Python (refer to requirement.txt file for the packages used in this project)
- Streamlit (interface for the model)


## Quick glance at the results

- Histogram to check the count of price per square feet -

![total_sqft](https://user-images.githubusercontent.com/87244972/176012947-ba6556e2-3a49-4eb1-9c10-fc7844dbb4ea.PNG)


- Histogram to check the count of BHK apartment -

![BHK](https://user-images.githubusercontent.com/87244972/176013200-7b7b9787-b8fe-48df-a6e0-c8d20cdace02.PNG)


- Histogram to check the count of number of washrooms - 

![bath](https://user-images.githubusercontent.com/87244972/176013304-c0f27d27-e6c5-4e8e-8b6b-dc2b229faf0a.PNG)


## Deployment on Streamlit

To deploy this project on streamlit share, follow these steps:

- First, make sure you upload your files on Github, including a requirements.txt file
- Go to [streamlit share](https://share.streamlit.io/)
- Login with Github, Google, etc.
- Click on new app button
- Select the Github repo name, branch, python file with the streamlit codes
- Click advanced settings, select python version 3.9 and add the secret keys if your model is stored on AWS or GCP bucket
- Then save and deploy!


## Repository structure

```

├── assets
│   ├── total_sqft.png                           <- Histogram showing price per sqaure feet.
│   ├── BHK.png                                  <- Image of Histogram showing total number of BHK's.
│   ├── bath.png                                 <- A picture of Histogram for total number of bahrooms.
│   ├── capture.png                              <- An image of web app interface.
│
├── dataset
│   ├── bengaluru_house_prices.csv               <- Raw data
│   ├── final_data.csv                           <- The data after Data Preparation
│ 
├── RealEstateNotebook.ipynb                     <- Main python notebook where all the analysis and modeling is done.
│
├── Columns.json                                 <- Json file where all the columns are stored.
│
├── Banglore_Home_Prices_Model.pickle            <- Pickle file of the model.
├
├── README.md                                    <- This is readme file.
│
├── app.py                                       <- File with the model and streamlit component for rendering the interface.
│
├── requirements.txt                             <- list of all the dependencies with their versions.

```
