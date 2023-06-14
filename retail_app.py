# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
st.set_page_config(page_title='SRetail EDA', layout='wide')



# Page header and information

st.subheader('Exploratory Data Analysis 📈')
st.write('© The Sparks Foundation')
st.title('Super Store Retail Analysis')

st.markdown('<hr>', unsafe_allow_html=True)
# Introduction and project overview
st.write('''In this EDA (Exploratory Data Analysis) project, the goal is to analyze retail data to identify weak areas within the business where improvements can be made to increase profitability. As a business manager, understanding the data and identifying key business problems is crucial for making informed decisions and implementing effective strategies.

Exploratory Data Analysis involves examining and visualizing the available data to gain insights, detect patterns, and uncover relationships. By conducting a thorough exploration of the retail dataset, several business problems can be derived. Here are some examples:

- Sales Performance: Analyzing sales data can reveal information about the performance of different products, categories, or departments. Identifying low-performing products or areas can help prioritize improvement efforts to increase sales and profitability.

- Customer Segmentation: Exploring customer data, such as demographics, purchase history, and behavior, can lead to insights about customer segments. Identifying high-value customer segments and understanding their preferences and buying patterns can help tailor marketing strategies and improve customer satisfaction.

- Inventory Management: Analyzing inventory data, including stock levels, turnover rates, and product demand, can help optimize inventory management. Identifying slow-moving or overstocked items can enable better planning and reduce costs associated with excess inventory.

- Pricing Analysis: Examining pricing data and comparing it with sales performance can provide insights into pricing strategies and their impact on customer demand. Identifying price-sensitive products or price points can help optimize pricing strategies for increased profitability.

- Store Performance: Analyzing store-level data, such as footfall, conversion rates, and average transaction value, can highlight underperforming stores or locations. Understanding the factors influencing store performance can guide decisions related to store layout, marketing efforts, or staff allocation.

- Seasonality and Trends: Exploring historical sales data can reveal seasonal patterns and trends that may impact business performance. Understanding these patterns can help plan promotions, stock inventory accordingly, and optimize resource allocation during peak periods.

- Marketing Effectiveness: Analyzing marketing campaign data, such as customer response rates, conversion rates, and ROI (Return on Investment), can provide insights into the effectiveness of different marketing initiatives. Identifying successful campaigns or channels can help allocate marketing budgets more efficiently.

By diving into the available retail data and employing various EDA techniques, these are just a few of the many business problems that can be derived. The ultimate objective is to uncover actionable insights that can drive improvements in different aspects of the retail business, leading to increased profitability and customer satisfaction.''')

st.markdown('<hr>', unsafe_allow_html=True)


st.subheader('Import all Libraries required')
st.markdown('<hr>', unsafe_allow_html=True)
a1='''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
'''
st.code(a1, language='python')
st.markdown('<hr>', unsafe_allow_html=True)
'\n'
'\n'

st.write('## Loading  the Dataset ')

st.code('''# load dataset
df = pd.read_csv('SampleSuperstore.csv')

# take a look at the first five rows
df.head()''', language='python')

import streamlit as st
import pandas as pd

# Path to the CSV file
csv_file_path = "C:\\Users\\Dell\\Documents\\Data Science\\Sparks Internship\\Super Store Reatail\\SampleSuperstore.csv"
# Read the CSV file
df = pd.read_csv(csv_file_path)

# Display the dataframe
st.dataframe(df)

st.markdown('<hr>', unsafe_allow_html=True)
'\n'
'\n'

st.code('''# Replace spaces with underscore in column names
df.rename(columns=lambda x: x.replace(' ', '_'), inplace=True)''', language='python')


# Rename columns
df.rename(columns=lambda x: x.replace(' ', '_'), inplace=True)

# Display the updated DataFrame
st.write(df)
'\n'
'\n'
st.markdown('<hr>', unsafe_allow_html=True)
st.subheader('Exploratory Data Analysis (EDA)')
'\n'
'\n'


st.code('''# Let's have a quick overview of the data distribution
df.describe().T''', language='python')
df.describe().T
'\n'
st.write('''##### There are 9994 recorded sales transactions in the dataset.


#### Sales:

Mean: The average sales amount is 229.858001, indicating the average value of sales.
Standard Deviation: Sales values exhibit significant variability with a standard deviation of 623.245101.
Minimum: The smallest recorded sales amount is 0.444, representing the lowest value in the dataset.
25th Percentile (Q1): 25% of the sales values fall below 17.28000.
Median (Q2): The median sales amount is 54.4900, representing the middle value in the dataset.
75th Percentile (Q3): 75% of the sales values fall below 209.940.
Maximum: The highest recorded sales amount is 22638.480.


#### Quantity:

Mean: On average, customers purchase approximately 3.789574 items per transaction.
Standard Deviation: The standard deviation of quantities purchased is 2.225110, indicating variability in customer purchase behavior.
Minimum: The minimum quantity purchased is 1, representing the lowest value in the dataset.
25th Percentile (Q1): 25% of the quantities fall below 2.00000.
Median (Q2): The median quantity is 3.0000, representing the middle value in the dataset.
75th Percentile (Q3): 75% of the quantities fall below 5.000.
Maximum: The highest recorded quantity is 14.


#### Discount:

Mean: On average, customers receive a discount of approximately 0.156203 on their purchases.
Standard Deviation: The standard deviation of discounts is 0.206452, indicating variability in the discount amounts.
Minimum: The minimum discount offered is 0.000, indicating that some transactions had no discount.
25th Percentile (Q1): 25% of the discounts fall below 0.00000.
Median (Q2): The median discount offered is 0.2000, representing the middle value in the dataset.
75th Percentile (Q3): 75% of the discounts fall below 0.200.
Maximum: The highest recorded discount is 0.800.


#### Profit:

Mean: On average, the profit per transaction is approximately 28.656896.
Standard Deviation: The standard deviation of profits is 234.260108, indicating variability in profit margins.
Minimum: The dataset contains negative profit values, with the lowest recorded profit being -6599.978.
25th Percentile (Q1): 25% of the profits fall below 1.72875.
Median (Q2): The median profit is 8.6665, representing the middle value in the dataset.
75th Percentile (Q3): 75% of the profits fall below 29.364.
Maximum: The highest recorded profit is 8399.976.



#### Conclusion:

Sales, quantity, discount, and profit analyses provide valuable information regarding average values, variability, and distribution.
Negative profits indicate potential areas of improvement for the business.
Further analysis and exploration of the dataset are recommended to identify patterns and potential areas for optimization.''')

'\n'
st.markdown('<hr>', unsafe_allow_html=True)

st.code('df.dtypes', language='python')
st.write(df.dtypes)
'\n'
st.write('''The dataset contains the following columns:

1. Ship_Mode: This column represents the mode of shipment for the products. It is an object data type, which typically means it contains textual or categorical information.

2. Segment: This column represents the segment of customers to which the sales belong. It is an object data type, indicating that it contains categorical information.

3. Country: This column contains the name of the country associated with the sales data. It is an object data type, indicating textual information.

4.City: This column contains the name of the city associated with the sales data. It is an object data type, representing textual information.

5. State: This column represents the state or region associated with the sales data. It is an object data type, typically containing textual information.

6. Postal_Code: This column represents the postal code associated with the sales data. It is an integer data type (int64), indicating numerical information.

7. Region: This column represents the region to which the sales data belongs. It is an object data type, containing categorical or textual information.

8. Category: This column represents the category of the products being sold. It is an object data type, indicating categorical information.

9. Sub-Category: This column represents the sub-category of the products being sold. It is an object data type, containing categorical or textual information.

10. Sales: This column represents the sales value associated with each data point. It is a float data type (float64), indicating numerical information with decimal precision.

These columns provide valuable information about the various aspects of the sales data, including shipping, customer segmentation, geographical details, product categories, and sales values. Analyzing these columns can help gain insights into the sales patterns and make informed business decisions.''')
st.markdown('<hr>', unsafe_allow_html=True)

st.code('df.isnull().sum()', language='python')
st.write(df.isnull().sum())

st.write('''# Summary:

Upon performing the `df.isnull().sum()` operation on the dataset, it is evident that there are no missing values in any of the columns. The result indicates that each column in the dataset, including Ship Mode, Segment, Country, City, State, Postal Code, Region, Category, Sub-Category, Sales, Quantity, Discount, and Profit, contains complete data with no null or missing entries.

This is good news as it suggests that the dataset is clean and suitable for analysis without the need for imputation or handling missing values. Having a complete dataset allows for more accurate and reliable analysis, as all the available information is present for each observation.

With a clean dataset, researchers and analysts can confidently proceed with various exploratory and statistical analyses, deriving meaningful insights and making informed decisions based on the complete information at hand.

However, further analysis may still be necessary to identify potential outliers, validate data integrity, and examine relationships between variables. The absence of missing values is an essential starting point for conducting thorough and accurate analyses on the given dataset.''')


st.code('''# Let\'s check dimensions of the DataFrame
df.shape''', language='python')

st.write(df.shape)
st.write('There are 13 columns and 9994 rows in the dataset')

st.code('''states = df.State.nunique()
print(f'Number of States: {states}')''', language='python')
st.write('Number of States:', df.State.nunique())
st.write('Out of the 50 states in USA, there were sales in 49 states')


st.code('''city = df.city.nunique()
print(f'Number of cities: {city}')''', language='python')
st.write('Number of cities:', df.City.nunique())
st.write('Sales occured across 531 cities in the United State')


st.code('display(df.Segment.unique())', language='python')
st.write(df.Segment.unique())
st.write('There are 3 different class for customer segment')















