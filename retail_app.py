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
df''', language='python')

import streamlit as st
import pandas as pd

# Path to the CSV file
csv_file_path = "https://raw.githubusercontent.com/Barde-S/Super-Store-Retail-EDA/main/SampleSuperstore.csv"
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
st.markdown('<hr>', unsafe_allow_html=True)

st.code('''# Let\'s check dimensions of the DataFrame
df.shape''', language='python')

st.markdown('<hr>', unsafe_allow_html=True)


st.write(df.shape)
st.write('There are 13 columns and 9994 rows in the dataset')

st.markdown('<hr>', unsafe_allow_html=True)


st.code('''states = df.State.nunique()
print(f'Number of States: {states}')''', language='python')
st.write('Number of States:', df.State.nunique())
st.write('Out of the 50 states in USA, there were sales in 49 states')

st.markdown('<hr>', unsafe_allow_html=True)


st.code('''city = df.city.nunique()
print(f'Number of cities: {city}')''', language='python')
st.write('Number of cities:', df.City.nunique())
st.write('Sales occured across 531 cities in the United State')

st.markdown('<hr>', unsafe_allow_html=True)



st.code('display(df.Segment.unique())', language='python')
st.write(df.Segment.unique())
st.write('There are 3 different class for customer segment')

st.markdown('<hr>', unsafe_allow_html=True)


st.code('''df['Category'].unique()''', language='python')
st.write(df['Category'].unique())
st.write('The store has 3 different categories of products')

st.markdown('<hr>', unsafe_allow_html=True)



st.code('''df.groupby('Category')['Sub-Category'].value_counts()''', language='python')
st.write(df.groupby('Category')['Sub-Category'].value_counts())

st.write('''1. Furniture Category:

- Furnishings: The most common sub-category in the Furniture category, with a count of 957.
- Chairs: The second most common sub-category in the Furniture category, with a count of 617.
- Tables: The third most common sub-category in the Furniture category, with a count of 319.
- Bookcases: A relatively less common sub-category in the Furniture category, with a count of 228.

2. Office Supplies Category:

- Binders: The most common sub-category in the Office Supplies category, with a count of 1523.
- Paper: The second most common sub-category in the Office Supplies category, with a count of 1370.
- Storage: The third most common sub-category in the Office Supplies category, with a count of 846.
- Art, Appliances, Labels, Envelopes, Fasteners, and Supplies: These sub-categories have varying counts, indicating their different levels of popularity within the Office Supplies category.

3. Technology Category:

- Phones: The most common sub-category in the Technology category, with a count of 889.
- Accessories: The second most common sub-category in the Technology category, with a count of 775.
- Machines: A relatively less common sub-category in the Technology category, with a count of 115.
- Copiers: The least common sub-category in the Technology category, with a count of 68.

Based on this analysis, we can observe that within each category, certain sub-categories are more prevalent than others. This information can be valuable for understanding the distribution of products within each category and can potentially be used for making business decisions related to inventory management, marketing strategies, and product offerings.''')

st.markdown('<hr>', unsafe_allow_html=True)



st.code('df.Ship_Mode.unique()', language='python')
st.write(df.Ship_Mode.unique())
st.write('''Under the shipping mode column, there are 4 different types of shipping modes:
1. Standard Class 
2. First Class
2. First Class
3. Second Class
4. Same Day''')

st.markdown('<hr>', unsafe_allow_html=True)



st.code('df.Region.unique()', language='python')
st.write(df.Region.unique())
st.write('The stores are situated across 4 regions of the US')

st.markdown('<hr>', unsafe_allow_html=True)



st.code('''# Heatmap to see corelation
sns.heatmap(df.corr(), annot=True)''', language='python')


fig, ax = plt.subplots(figsize=(5, 3))  # Adjust the figsize according to your desired size

# Generate the heatmap
heatmap = sns.heatmap(df.corr(), annot=True, ax=ax)

# Set the width of the plot frame
plt.tight_layout()

# Display the heatmap in Streamlit
st.pyplot(fig)

st.write('''The heatmap above is a bit not too clear. This is due to the negative values in the Profit columns. It would be better if it is split into Gain and Loss. Doing this would provide the better information we need.''')
'\n'
st.markdown('<hr>', unsafe_allow_html=True)

st.code('''# Creating new dataframe df2 from the former df
df2 = df.copy()

# Create 'Gain' and 'Loss' columns
df2['Gain'] = df2['Profit'].apply(lambda x: x if x > 0 else 0)
df2['Loss'] = df2['Profit'].apply(lambda x: x if x <= 0 else 0)

df2.shape''', language='python')

# Creating new dataframe df2 from the former df
df2 = df.copy()

# Create 'Gain' and 'Loss' columns
df2['Gain'] = df2['Profit'].apply(lambda x: x if x > 0 else 0)
df2['Loss'] = df2['Profit'].apply(lambda x: x if x <= 0 else 0)

df2.shape

st.write('''I decided to create a new dataframe df2 with new columns Gain and Loss from the profit column. We now have 15 columns, 2 greater than the former with 13.\n
I considered any entry that is equal or less than zero as loss, and any greater than zero as gain''' )

st.markdown('<hr>', unsafe_allow_html=True)

st.code('''# drop the minus sign in the loss column
df2['Loss'] = df2['Loss'].abs()

# let drop some columns that are surplus of need
df2= df2.drop(columns=['Profit', 'Country', 'Postal_Code'])''', language='python')

# drop the minus sign in the loss column
df2['Loss'] = df2['Loss'].abs()

# let drop some columns that are surplus of need
df2= df2.drop(columns=['Profit', 'Country', 'Postal_Code'])

st.write('''I decided to turn the Loss column to positive. This is because it will affect the analysis. 

However, i dropped some columns which are of no use to the analysis. (Profit, Country, and Postal code)''')

st.markdown('<hr>', unsafe_allow_html=True)
st.code('''# Let's take a look at our new dataset
df2.head()''', language='python')


# Let's take a look at our new dataset
st.write(df2.head())


st.markdown('<hr>', unsafe_allow_html=True)

st.code('''# Let's see a summary stat on the new dataset df2
df2.describe().T''', language='python')

st.write(# Let's see a summary stat on the new dataset df2
df2.describe().T)
'\n'
st.write('''Now we have a clearer image of our data than the former one.

Summary of the new Dataset Variables:

Sales:
- Mean: The average sales amount is approximately $229.858001, indicating the typical value of sales transactions.
- Standard Deviation: Sales values exhibit a significant amount of variability, with a standard deviation of approximately $623.245101.
- Minimum: The smallest recorded sales amount is $0.444, representing the lowest value in the dataset.
- 25th Percentile (Q1): 25% of the sales values fall below $17.28000.
- Median (Q2): The median sales amount is $54.4900, representing the middle value in the dataset.
- 75th Percentile (Q3): 75% of the sales values fall below $209.940.
- Maximum: The highest recorded sales amount is $22638.480.

Quantity:
- Mean: On average, customers purchase approximately 3.789574 items per transaction.
- Standard Deviation: The standard deviation of quantities purchased is 2.225110, indicating variability in customer purchase behavior.
- Minimum: The minimum quantity purchased is 1, representing the lowest value in the dataset.
- 25th Percentile (Q1): 25% of the quantities fall below 2.00000.
- Median (Q2): The median quantity is 3.0000, representing the middle value in the dataset.
- 75th Percentile (Q3): 75% of the quantities fall below 5.000.
- Maximum: The highest recorded quantity is 14.

Discount:
- Mean: On average, customers receive a discount of approximately 0.156203 on their purchases.
- Standard Deviation: The standard deviation of discounts is 0.206452%, indicating variability in the discount amounts.
- Minimum: The minimum discount offered is 0.000%, indicating that some transactions had no discount.
- 25th Percentile (Q1): 25% of the discounts fall below 0.00000%.
- Median (Q2): The median discount offered is 0.2000%, representing the middle value in the dataset.
- 75th Percentile (Q3): 75% of the discounts fall below 0.200%.
- Maximum: The highest recorded discount is 0.800%.

Gain:
- Mean: The average gain per transaction is approximately $44.279398.
- Standard Deviation: The standard deviation of gains is $193.122144, indicating variability in the profit margins.
- Minimum: The dataset contains gains ranging from $0.000, representing the lowest recorded gain.
- 25th Percentile (Q1): 25% of the gains fall below $1.72875.
- Median (Q2): The median gain is $8.6665, representing the middle value in the dataset.
- 75th Percentile (Q3): 75% of the gains fall below $29.364.
- Maximum: The highest recorded gain is $8399.976.

Loss:
- Mean: The average loss per transaction is approximately $15.622502.
- Standard Deviation: The standard deviation of losses is $127.271313, indicating variability in the losses incurred.
- Minimum: The dataset contains losses ranging from 0.000, representing the lowest recorded loss.
- 25th Percentile (Q1): 25% of the losses fall below 0.00000.
- Median (Q2): The median loss is 0.0000, representing the middle value in the dataset.
- 75th Percentile (Q3): 75% of the losses fall below 0.000.
- Maximum: The highest recorded loss in a single sales is $6599.978.

Overall Analysis:
- The dataset consists of 9994 observations and provides insights into sales, quantity, discount, gain, and loss analysis.
- Sales values vary greatly, with a wide range of values and significant variability, as indicated by the high standard deviation.
- Quantity analysis reveals that customers generally purchase a moderate number of items per transaction, with a mean value close to the median.
- Discounts offered to customers show variability, with some transactions having no discount while others have discounts ranging from 0.000 to 0.800.
- Gain and loss analysis demonstrates the variability in profit margins, with a wide range of values and considerable variability in gains and losses.
- Further analysis and exploration of the dataset are recommended to identify patterns, relationships, and potential areas for improvement.

''')

st.markdown('<hr>', unsafe_allow_html=True)

st.code('''sns.heatmap(df2.corr(), annot=True)
plt.show()''', language='python')



fig, ax = plt.subplots(figsize=(5, 3))  # Adjust the figsize according to your desired size

# Generate the heatmap
heatmap = sns.heatmap(df2.corr(), annot=True, ax=ax)

# Set the width of the plot frame
plt.tight_layout()

# Display the heatmap in Streamlit
st.pyplot(fig)

st.write('''From the Plot above we can deduce
- Discount does not improve sales
- Decent number of stores recorded loss
- There is no much correlation between the quantity of product purchase with both gain and loss
- Discount does not make customers to purchase more products''')

st.code('''# Lets see how many sales made gain and loss
gains_count = len(df[df['Profit'] > 0])  

losses_count = len(df[df['Profit'] <= 0])  

print("Number of gains:", gains_count)
print("Number of losses:", losses_count)

total_count = len(df)
gains_percentage = gains_count / total_count * 100
losses_percentage = losses_count / total_count * 100

# Create the pie chart
labels = ['Gains', 'Losses']
percentages = [gains_percentage, losses_percentage]
colors = ['orangered', 'deepskyblue']
explode = (0.1, 0)  # Use explode to highlight a slice

plt.pie(percentages, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
plt.title('Percentage of Gains and Losses')
plt.show()''', language='python')

# Calculate the number of gains and losses
gains_count = len(df[df['Profit'] > 0])
losses_count = len(df[df['Profit'] <= 0])

# Calculate the percentages
total_count = len(df)
gains_percentage = gains_count / total_count * 100
losses_percentage = losses_count / total_count * 100

# Create the pie chart
labels = ['Gains', 'Losses']
percentages = [gains_percentage, losses_percentage]
colors = ['orangered', 'deepskyblue']
explode = (0.1, 0)  # Use explode to highlight a slice

# Display the number of gains and losses
st.write("Number of gains:", gains_count)
st.write("Number of losses:", losses_count)

# Display the pie chart
fig, ax = plt.subplots(figsize=(6, 4))
ax.pie(percentages, explode=explode, labels=labels, colors=colors,
       autopct='%1.1f%%', shadow=True, startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
ax.set_title('Percentage of Gains and Losses')

# Display the chart in Streamlit
st.pyplot(fig)

st.write('From the plot above we can see that sales recorded 81% gain, and 19% loss.')

st.markdown('<hr>', unsafe_allow_html=True)

st.write('Let\'s have pairwise relationships plot in a dataset')

st.code('''sns.pairplot(df2)
plt.show()''', language='python')


# Display the pairplot
fig = sns.pairplot(df2)
st.pyplot(fig)


st.markdown('<hr>', unsafe_allow_html=True)

st.code('''# Let's see distribution of sales base on category
display(df2.groupby('Category')['Category'].count())
sns.countplot(data=df2, x='Category', order=['Office Supplies', 'Furniture', 'Technology'])
plt.show()''', language='python')

# Display the count of each category
category_counts = df2['Category'].value_counts()
st.write(category_counts)

# Create a count plot
fig, ax = plt.subplots(figsize=(6, 4))
sns.countplot(data=df2, x='Category', order=['Office Supplies', 'Furniture', 'Technology'])
plt.title('Distribution of Sales by Category')
plt.xlabel('Category')
plt.ylabel('Count')
plt.xticks(rotation=90)
st.pyplot(fig)

st.write('''From the diagram above we can deduce that products under the category of Office supplies were sold more. A total purchase of 6026 were made, followed by furniture with a total purchase of 2121 then finally technology with a total sale of 1847''')

st.markdown('<hr>', unsafe_allow_html=True)

st.code('''
category_counts = df2['Segment'].value_counts()
plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%')
plt.axis('equal')
plt.title('Pie Chart of Segment Distribution')
plt.show()
''', language='python')
# Get the value counts of each segment
category_counts = df2['Segment'].value_counts()

# Create the pie chart
fig, ax = plt.subplots()
ax.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%')
ax.axis('equal')
ax.set_title('Pie Chart of Segment Distribution')

# Display the plot in Streamlit
st.pyplot(fig)

st.write('Under segment, from above you can see that Consumers are the most frequent patronizers then Corporate and then home office')
st.markdown('<hr>', unsafe_allow_html=True)

st.code('''color=['purple', 'blue', 'black']
seg_loss = df2.groupby('Segment')['Loss'].sum()

display(seg_loss)

seg_loss.plot(kind='bar', color=color)''', language='python')

# Define the colors for the bars
colors = ['purple', 'blue', 'black']

# Group the loss by segment and calculate the sum
seg_loss = df2.groupby('Segment')['Loss'].sum()

# Display the loss values
st.write(seg_loss)

# Create the bar chart
fig, ax = plt.subplots()
seg_loss.plot(kind='bar', color=colors)

# Customize the plot
ax.set_xlabel('Segment')
ax.set_ylabel('Loss')
ax.set_title('Loss by Segment')

# Display the plot in Streamlit
st.pyplot(fig)

st.write('More loss were recorded on the consumer segment')


st.code('''color=['brown', 'grey', 'violet']
seg_gain = df2.groupby('Segment')['Gain'].sum()

display(seg_gain)

seg_gain.plot(kind='bar', color=color)''', language='python')


# Define the colors for the bars
colors = color=['brown', 'grey', 'violet']

# Group the loss by segment and calculate the sum
seg_loss = df2.groupby('Segment')['Gain'].sum()

# Display the loss values
st.write(seg_loss)

# Create the bar chart
fig, ax = plt.subplots()
seg_loss.plot(kind='bar', color=colors)

# Customize the plot
ax.set_xlabel('Segment')
ax.set_ylabel('Gain')
ax.set_title('Loss by Segment')

# Display the plot in Streamlit
st.pyplot(fig)

st.write('''Again there are more loss under the consumer segment. This is due to the fact that more consumers made purchase of products. It is interesting to see that a significant gain were made under the corporate segment too.''')
st.markdown('<hr>', unsafe_allow_html=True)


st.code('''scolor = ['red', 'blue', 'green']
display(df2.groupby('Category')['Sales'].sum().sort_values(ascending=False).to_frame())
df.groupby('Category')['Sales'].sum().sort_values(ascending=False).plot(kind='bar', color=color)
plt.title('Total sales in each category')
plt.ylabel('Sales')
plt.show()''', language='python')


color = ['red', 'blue', 'green']
st.write(df2.groupby('Category')['Sales'].sum().sort_values(ascending=False).to_frame())


fig, ax = plt.subplots()
df.groupby('Category')['Sales'].sum().sort_values(ascending=False).plot(kind='bar', color=color)
ax.set_title('Total sales in each category')
ax.set_ylabel('Sales')
st.pyplot(fig)

st.write('''All the categories performed almost the same interms of sales, they are all not far from each other.
- Technology: $836154.0330
- Furniture: $741999.7953
- Office Supplies: $719047.0320

''')
st.markdown('<hr>', unsafe_allow_html=True)

st.code('''df2.groupby('State')['Loss'].sum().sort_values(ascending=False).to_frame()''', language='python')
df2.groupby('State')['Loss'].sum().sort_values(ascending=False).to_frame()

st.write('''When it comes to loss based on states a lot of states recorded significant loss. However the top 10 states with most loss are:
- Texas: $36813.1875
- Ohio: $21750.0002
- Pennsylvania:	$21602.8515
- Illinois:	$19501.6975
- North Carolina: $1557.9854
- Colorado:	$8900.9048
- Florida: $8689.8295
- Tennessee: $7257.0174
- Arizona: $6656.7675
- New York:	$5031.1378
''')

st.markdown('<hr>', unsafe_allow_html=True)
st.code('''cat_by_state = df2.groupby(['State', 'Category'])['Loss'].sum().sort_values(ascending=False)
display(cat_by_state.head(50).to_frame())''', language='pythin')
cat_by_state = df2.groupby(['State', 'Category'])['Loss'].sum().sort_values(ascending=False)
st.write(cat_by_state.head(50).to_frame())

st.write('''The output shows that the states with the highest losses in office supplies are Texas, Ohio, and Illinois. The states with the highest losses in furniture are Texas, Pennsylvania, and New York. The states with the highest losses in technology are Ohio, Colorado, and California.

This suggests that there may be some areas where the company could improve its inventory management or loss prevention practices. For example, the company could consider implementing a more robust inventory tracking system to ensure that all office supplies are accounted for. The company could also consider installing security cameras in high-traffic areas to deter theft.

Overall, the output of your code provides some valuable insights into where the company is losing money. By taking steps to address these areas, the company can reduce its losses and improve its bottom line.

Here are some additional thoughts on how the company could improve its loss prevention practices:

1. Implement a more robust inventory tracking system. This would help the company to identify areas where inventory is being lost or stolen.
2. Install security cameras in high-traffic areas. This would deter theft and make it easier to identify perpetrators.
Create a loss prevention policy and train employees on how to implement it. This would help employees to understand their role in preventing losses.
3. Conduct regular audits of inventory levels. This would help the company to identify any discrepancies early on.
4. Work with law enforcement to investigate thefts. This would help to deter future thefts and bring perpetrators to justice.
By taking these steps, the company can reduce its losses and improve its bottom line.1. ''')

st.markdown('<hr>', unsafe_allow_html=True)
st.code('''display('Texas', df2[df2['State'] == 'Texas'].groupby('Category')['Loss'].sum().to_frame().T)
display('Ohio', df2[df2['State'] == 'Ohio'].groupby('Category')['Loss'].sum().to_frame().T)
display('Pennsylvania', df2[df2['State'] == 'Pennsylvania'].groupby('Category')['Loss'].sum().to_frame().T)
display('Illinois', df2[df2['State'] == 'Illinois'].groupby('Category')['Loss'].sum().to_frame().T)
display('North Carolina', df2[df2['State'] == 'North Carolina'].groupby('Category')['Loss'].sum().to_frame().T)
display('Colarado', df2[df2['State'] == 'Colorado'].groupby('Category')['Loss'].sum().to_frame().T)
display('Tennesse', df2[df2['State'] == 'Tennessee'].groupby('Category')['Loss'].sum().to_frame().T)
display('Arizona', df2[df2['State'] == 'Arizona'].groupby('Category')['Loss'].sum().to_frame().T)
display('Florida', df2[df2['State'] == 'Florida'].groupby('Category')['Loss'].sum().to_frame().T)
display('Oregon', df2[df2['State'] == 'Oregon'].groupby('Category')['Loss'].sum().to_frame().T)
''')


st.write('Texas', df2[df2['State'] == 'Texas'].groupby('Category')['Loss'].sum().to_frame().T)
st.write('Ohio', df2[df2['State'] == 'Ohio'].groupby('Category')['Loss'].sum().to_frame().T)
st.write('Pennsylvania', df2[df2['State'] == 'Pennsylvania'].groupby('Category')['Loss'].sum().to_frame().T)
st.write('Illinois', df2[df2['State'] == 'Illinois'].groupby('Category')['Loss'].sum().to_frame().T)
st.write('North Carolina', df2[df2['State'] == 'North Carolina'].groupby('Category')['Loss'].sum().to_frame().T)
st.write('Colarado', df2[df2['State'] == 'Colorado'].groupby('Category')['Loss'].sum().to_frame().T)
st.write('Tennesse', df2[df2['State'] == 'Tennessee'].groupby('Category')['Loss'].sum().to_frame().T)
st.write('Arizona', df2[df2['State'] == 'Arizona'].groupby('Category')['Loss'].sum().to_frame().T)
st.write('Florida', df2[df2['State'] == 'Florida'].groupby('Category')['Loss'].sum().to_frame().T)
st.write('Oregon', df2[df2['State'] == 'Oregon'].groupby('Category')['Loss'].sum().to_frame().T)

st.write('''I decide to take the top 10 states with the most loss and here is the report:

The data shows that Texas, Ohio, Pennsylvania, Illinois, North Carolina, Colorado, Tennessee, Arizona, Florida, and Oregon have the highest losses in office supplies, furniture, and technology. This suggests that there may be some areas where these states could improve their inventory management or loss prevention practices.

For example, the states could consider implementing a more robust inventory tracking system to ensure that all office supplies are accounted for. The states could also consider installing security cameras in high-traffic areas to deter theft.

Overall, the data provides some valuable insights into where these states are losing money. By taking steps to address these areas, the states can reduce their losses and improve their bottom lines.

Here are some additional thoughts on how the states could improve their loss prevention practices:

Implement a more robust inventory tracking system. This would help the states to identify areas where inventory is being lost or stolen.
Install security cameras in high-traffic areas. This would deter theft and make it easier to identify perpetrators.
Create a loss prevention policy and train employees on how to implement it. This would help employees to understand their role in preventing losses.
Conduct regular audits of inventory levels. This would help the states to identify any discrepancies early on.
Work with law enforcement to investigate thefts. This would help to deter future thefts and bring perpetrators to justice.
By taking these steps, the states can reduce their losses and improve their bottom lines.

Here are some specific recommendations for each state:

- Texas: The state could consider implementing a more robust inventory tracking system for office supplies. The state could also consider installing security cameras in high-traffic areas, such as warehouses and distribution centers.
- Ohio: The state could consider implementing a more robust inventory tracking system for furniture. The state could also consider installing security cameras in high-traffic areas, such as furniture stores and showrooms.
- Pennsylvania: The state could consider implementing a more robust inventory tracking system for technology. The state could also consider installing security cameras in high-traffic areas, such as computer stores and electronics retailers.
- Illinois: The state could consider implementing a more robust inventory tracking system for office supplies and furniture. The state could also consider installing security cameras in high-traffic areas, such as warehouses, distribution centers, furniture stores, and showrooms.
- North Carolina: The state could consider implementing a more robust inventory tracking system for office supplies and technology. The state could also consider installing security cameras in high-traffic areas, such as warehouses, distribution centers, computer stores, and electronics retailers.
- Colorado: The state could consider implementing a more robust inventory tracking system for furniture and technology. The state could also consider installing security cameras in high-traffic areas, such as furniture stores, showrooms, computer stores, and electronics retailers.
- Tennessee: The state could consider implementing a more robust inventory tracking system for furniture and office supplies. The state could also consider installing security cameras in high-traffic areas, such as furniture stores, showrooms, warehouses, distribution centers, and office supply stores.
- Arizona: The state could consider implementing a more robust inventory tracking system for technology and office supplies. The state could also consider installing security cameras in high-traffic areas, such as computer stores, electronics retailers, warehouses, distribution centers, and office supply stores.
- Florida: The state could consider implementing a more robust inventory tracking system for all three categories. The state could also consider installing security cameras in high-traffic areas, such as warehouses, distribution centers, furniture stores, showrooms, computer stores, electronics retailers, and office supply stores.
- Oregon: The state could consider implementing a more robust inventory tracking system for technology and furniture. The state could also consider installing security cameras in high-traffic areas, such as computer stores, electronics retailers, furniture stores, and showrooms.''')

st.markdown('<hr>', unsafe_allow_html=True)

st.code('''color=['green', 'blue', 'black', 'red']
df2.groupby('Region')['Loss'].sum().sort_values(ascending=False).plot(kind='bar', color=color)''', language='python')

color=['green', 'blue', 'black', 'red']
fig, ax = plt.subplots()
df2.groupby('Region')['Loss'].sum().sort_values(ascending=False).plot(kind='bar', color=color)
ax.set_title('Total Loss in region category')
ax.set_ylabel('Loss')
st.pyplot(fig)

st.markdown('<hr>', unsafe_allow_html=True)

st.code('''df2.groupby('Region')['Loss'].sum().sort_values(ascending=False).plot(kind='bar', color=color)''', language='python')

fig, ax = plt.subplots()
sns.barplot(data=df2, x='Region', y='Sales', ci=None, order=['South', 'East', 'West', 'Central'])
ax.set_title('Total sales in region category')
ax.set_ylabel('Sales')
ax.set_xlabel('Region')
st.pyplot(fig)

st.markdown('<hr>', unsafe_allow_html=True)

st.code('''df2.groupby(['Region', 'Category'])['Sales'].count().to_frame()''', language='python')
st.write(df2.groupby(['Region', 'Category'])['Sales'].count().to_frame())
st.write('''The provided output shows the count of sales for each combination of regions and categories in the dataset. It provides valuable insights into the distribution of sales across different regions and categories, allowing us to identify patterns and trends.

The analysis reveals the following observations:

Central Region:

Furniture: There were 481 sales of furniture products in the Central region. 
Office Supplies: The count for office supplies sales was 1,422. 
Technology: The technology category had 420 sales. 

East Region:

Furniture: The count of furniture sales in the East region was 601. 
Office Supplies: There were 1,712 sales of office supplies.
Technology: The technology category had 535 sales. 

South Region:

Furniture: The count for furniture sales in the South region was 332. 
Office Supplies: There were 995 sales of office supplies. 
Technology: The technology category had 293 sales. 

West Region:

- Furniture: The count of furniture sales in the West region was 707.
- Office Supplies: There were 1,897 sales of office supplies.
- Technology: The technology category had 599 sales.
These findings allow us to compare the sales distribution among different regions and categories. For example, we can observe that the East and West regions have higher sales counts across all categories compared to the Central and South regions. Additionally, the office supplies category appears to have the highest sales count in all regions.

This information can be valuable for various purposes, such as identifying the most popular product categories in each region, evaluating sales performance across different regions, and making informed business decisions based on regional sales patterns.

Overall, the provided analysis of sales counts by region and category offers a comprehensive understanding of the dataset and serves as a foundation for further exploration and decision-making.''')

st.markdown('<hr>', unsafe_allow_html=True)

st.code('''df2.groupby(['Region', 'Category'])['Sales'].sum().to_frame()''', language='python')
st.write(df2.groupby(['Region', 'Category'])['Sales'].sum().to_frame())

st.write('''The data shows that the East region has the highest sales in all three categories, followed by the West region, the Central region, and the South region.

This suggests that there may be some areas where different regions could improve their sales. For example, the South region could consider increasing its marketing efforts for furniture and technology. The Central region could consider increasing its marketing efforts for office supplies and technology.

Overall, the data provides some valuable insights into where different regions are performing well and where they could improve. By taking steps to address these areas, different regions can increase their sales and improve their bottom lines.

Here are some specific recommendations for each region:

- East region: The East region could consider increasing its marketing efforts for furniture and technology. The region could also consider offering a wider variety of furniture styles and brands, as well as a wider variety of technology brands and models.
- West region: The West region could consider increasing its marketing efforts for all three categories. The region could also consider offering a wider variety of products and services in all three categories.
- Central region: The Central region could consider increasing its marketing efforts for office supplies and technology. The region could also consider offering a wider variety of office supplies brands and sizes, as well as a wider variety of technology brands and models.
- South region: The South region could consider increasing its marketing efforts for furniture and technology. The region could also consider offering a wider variety of furniture styles and brands, as well as a wider variety of technology brands and models.''')

st.markdown('<hr>', unsafe_allow_html=True)
st.code('''df2.groupby(['Region', 'Category'])['Loss'].sum().to_frame()''', language='python')
st.write(df2.groupby(['Region', 'Category'])['Loss'].sum().to_frame())
st.write('''The data shows that the Central region has the highest losses in all three categories, followed by the East region, the South region, and the West region.

This suggests that there may be some areas where different regions could improve their profitability. For example, the South region could consider reducing its costs for furniture and technology. The Central region could consider reducing its costs for office supplies and technology.

Overall, the data provides some valuable insights into where different regions are performing poorly and where they could improve. By taking steps to address these areas, different regions can improve their profitability and bottom lines.

Here are some specific recommendations for each region:

- Central region: The Central region could consider reducing its costs for furniture by negotiating better prices with suppliers, reducing waste, and improving efficiency. The region could also consider reducing its costs for office supplies by negotiating better prices with suppliers, reducing waste, and improving efficiency. The region could also consider reducing its costs for technology by negotiating better prices with suppliers, reducing waste, and improving efficiency.
- East region: The East region could consider reducing its costs for furniture by negotiating better prices with suppliers, reducing waste, and improving efficiency. The region could also consider reducing its costs for office supplies by negotiating better prices with suppliers, reducing waste, and improving efficiency. The region could also consider reducing its costs for technology by negotiating better prices with suppliers, reducing waste, and improving efficiency.
- South region: The South region could consider reducing its costs for furniture by negotiating better prices with suppliers, reducing waste, and improving efficiency. The region could also consider reducing its costs for office supplies by negotiating better prices with suppliers, reducing waste, and improving efficiency. The region could also consider reducing its costs for technology by negotiating better prices with suppliers, reducing waste, and improving efficiency.
- West region: The West region could consider reducing its costs for furniture by negotiating better prices with suppliers, reducing waste, and improving efficiency. The region could also consider reducing its costs for office supplies by negotiating better prices with suppliers, reducing waste, and improving efficiency. The region could also consider reducing its costs for technology by negotiating better prices with suppliers, reducing waste, and improving efficiency.

Here are some additional thoughts on how the regions can improve their profitability:

- Reduce costs: The regions can reduce costs by negotiating better prices with suppliers, reducing waste, and improving efficiency.
- Increase sales: The regions can increase sales by increasing their marketing efforts, offering a wider variety of products and services, and providing excellent customer service.
- Improve efficiency: The regions can improve efficiency by streamlining their operations, using technology to automate tasks, and empowering their employees to make decisions.
By taking these steps, the regions can improve their profitability and bottom lines.''')

st.markdown('<hr>', unsafe_allow_html=True)


st.code('''central = df2[df2['Region']=='Central'].groupby('State')['Loss'].sum().sort_values(ascending=False)
display(central.to_frame())

plt.title('Loss made by state in Central US')
central.plot(kind='bar')
plt.ylabel('Loss')
pltxlabel('States in Central America')
plt.show()''', language='python')

central = df2[df2['Region']=='Central'].groupby('State')['Loss'].sum().sort_values(ascending=False)
st.write(central.to_frame())

fig, ax = plt.subplots()
central.plot(kind='bar')
ax.set_title('Loss made in each State in Central US')
ax.set_ylabel('Loss')
ax.set_xlabel('States in Central America')
st.pyplot(fig)

st.write('''The data shows that Texas has the highest total loss value in the Central region, amounting to $36813.1875. Illinois follows with a total loss of $19501.6975. On the other hand, the remaining states in the Central region, including Indiana, Iowa, Kansas, Michigan, Minnesota, Missouri, Nebraska, North Dakota, Oklahoma, South Dakota, and Wisconsin, did not incur any losses based on the available data.''')
st.markdown('<hr>', unsafe_allow_html=True)

st.code('''central = df2[df2['Region']=='Central'].groupby('State')['Loss'].sum().sort_values(ascending=False)
display(central.to_frame())

plt.title('Loss made by state in Central US')
central.plot(kind='bar')
plt.ylabel('Loss')
pltxlabel('States in Central America')
plt.show()''', language='python')

south = df2[df2['Region']=='South'].groupby('State')['Loss'].sum().sort_values(ascending=False)
st.write(central.to_frame())

fig, ax = plt.subplots()
south.plot(kind='bar')
ax.set_title('Loss made in eacch State in Southern US')
ax.set_ylabel('Loss')
ax.set_xlabel('States in South of America')
st.pyplot(fig)

st.write('''According to the data, the states in the Southern region experienced varying levels of losses. North Carolina recorded the highest total loss value of $11557.9854, followed by Florida with 8689.8295 and Tennessee with $7257.0174. On the other hand, the remaining states in the Southern region, including Alabama, Arkansas, Georgia, Kentucky, Louisiana, Mississippi, South Carolina, and Virginia, did not report any losses during the specified period.''')

st.markdown('<hr>', unsafe_allow_html=True)

st.code('''west = df2[df2['Region']=='West'].groupby('State')['Loss'].sum().sort_values(ascending=False)
display(central.to_frame())

plt.title('Loss made by state in Western US')
central.plot(kind='bar')
plt.ylabel('Loss')
pltxlabel('States in Western America')
plt.show()''', language='python')

west = df2[df2['Region']=='West'].groupby('State')['Loss'].sum().sort_values(ascending=False)
st.write(west.to_frame())

fig, ax = plt.subplots()
west.plot(kind='bar')
ax.set_title('Loss made in eacch State of Western US')
ax.set_ylabel('Loss')
ax.set_xlabel('States in West of America')
st.pyplot(fig)

st.write('''According to the data, the states in the Western region experienced varying levels of losses. Colorado recorded the highest total loss value of $8900.9048, followed by Arizona with $6656.7675 and California with $3769.6651. Oregon and Washington also reported significant losses of $2890.4764 and $387.8706, respectively. Nevada and New Mexico experienced relatively lower losses with values of $109.5822 and $5.6943, respectively.

On the other hand, the states of Idaho, Montana, Utah, and Wyoming did not report any losses during the specified period.''')

st.markdown('<hr>', unsafe_allow_html=True)

st.code('''east = df2[df2['Region']=='East'].groupby('State')['Loss'].sum().sort_values(ascending=False)
display(east.to_frame())

plt.title('Loss made by state in Eastern US')
central.plot(kind='bar')
plt.ylabel('Loss')
pltxlabel('States in East of America')
plt.show()''', language='python')

east = df2[df2['Region']=='East'].groupby('State')['Loss'].sum().sort_values(ascending=False)
st.write(east.to_frame())

fig, ax = plt.subplots()
west.plot(kind='bar')
ax.set_title('Loss made in eacch State of East US')
ax.set_ylabel('Loss')
ax.set_xlabel('States in East of America')
st.pyplot(fig)

st.write('''According to the provided data, the states in the Eastern region experienced different levels of losses. Ohio reported the highest total loss value of $21750.0002, followed closely by Pennsylvania with $21602.8515. New York recorded losses amounting to $5031.1378, while Massachusetts and Rhode Island had loss values of $566.2617 and $230.1678, respectively.

New Hampshire, Delaware, West Virginia, Maryland, and New Jersey also experienced losses, albeit at relatively lower levels. Connecticut, District of Columbia, Maine, and Vermont did not report any losses during the specified period.''')



st.code('''nan = df2.groupby('Category')['Sub-Category'].value_counts().to_frame()
nan.rename(columns={'Sub-Category': 'Total number of product sold'}, inplace=True)
nan.rename_axis(['Category', 'Sub Category'], inplace=True)
nan''', language='python')

nan = df2.groupby('Category')['Sub-Category'].value_counts().to_frame()
nan.rename(columns={'Sub-Category': 'Total number of product sold'}, inplace=True)
nan.rename_axis(['Category', 'Sub Category'], inplace=True)
st.write(nan)

st.write('''The data shows that the most popular sub-category in furniture is furnishings, followed by chairs, tables, and bookcases. The most popular sub-category in office supplies is binders, followed by paper, storage, art, appliances, labels, envelopes, fasteners, and supplies. The most popular sub-category in technology is phones, followed by accessories, machines, and copiers.

This suggests that there may be some areas where the company could focus its marketing efforts. For example, the company could consider increasing its marketing efforts for furnishings in the furniture category. The company could also consider increasing its marketing efforts for binders in the office supplies category. The company could also consider increasing its marketing efforts for phones in the technology category.

Overall, the data provides some valuable insights into what products are popular with customers. By focusing its marketing efforts on these products, the company can increase its sales and improve its bottom line.

Here are some specific recommendations for the company:

- Furniture: The company could consider increasing its marketing efforts for furnishings by advertising in more print and online publications, attending trade shows, and sponsoring events. The company could also consider offering discounts or promotions on furnishings.
- Office Supplies: The company could consider increasing its marketing efforts for binders by advertising in more print and online publications, attending trade shows, and sponsoring events. The company could also consider offering discounts or promotions on binders.
- Technology: The company could consider increasing its marketing efforts for phones by advertising in more print and online publications, attending trade shows, and sponsoring events. The company could also consider offering discounts or promotions on phones.

Here are some additional thoughts on how the company can increase its sales:

1. Focus on popular products: The company can focus its marketing efforts on popular products, such as furnishings, binders, and phones.
2. Offer discounts or promotions: The company can offer discounts or promotions on popular products to attract new customers and encourage existing customers to buy more.
3. Improve customer service: The company can improve customer service by providing more training for its employees, implementing a customer satisfaction tracking system, and responding to customer complaints promptly.
4. Provide excellent value: The company can provide excellent value by offering competitive prices, high-quality products, and excellent customer service.
By taking these steps, the company can increase its sales and improve its bottom line.''')

st.markdown('<hr>', unsafe_allow_html=True)

st.code('''list = df2[['Region', 'Discount', 'Sales']]
a = list.groupby(['Region', 'Discount']).size().reset_index(name='Count')
new_list = a.pivot_table(index='Region', columns='Discount', values='Count')
new_list''')

z = df2[['Region', 'Discount', 'Sales']]
a = z.groupby(['Region', 'Discount']).size().reset_index(name='Count')
b = a.pivot_table(index='Region', columns='Discount', values='Count')
st.write(b)
st.markdown('<hr>', unsafe_allow_html=True)

st.code('''ship_loss = df2.groupby('Ship_Mode')['Loss'].sum()

display(ship_loss)

plt.pie(ship_loss, labels=ship_loss.index, autopct='%1.1f%%')
plt.axis('equal')
plt.title(' Distribution of Loss base on Shipping Mode ')
plt.show()
 ''', language='python')

ship_loss = df2.groupby('Ship_Mode')['Loss'].sum()

st.write(ship_loss)
fig, ax = plt.subplots()
plt.pie(ship_loss, labels=ship_loss.index, autopct='%1.1f%%')
ax.axis('equal')
ax.set_title(' Distribution of Loss base on Shipping Mode ')
st.pyplot(fig)

st.markdown('<hr>', unsafe_allow_html=True)

st.code('''ship_loss = df2.groupby('Ship_Mode')['Ship_Mode'].value_counts()
display(ship_loss)
plt.figure(figsize=[6,6])
ship_loss.plot(kind='bar')''', language='python')

st.markdown('<hr>', unsafe_allow_html=True)

st.code('''ship_loss = df2.groupby('Ship_Mode')['Ship_Mode'].value_counts()
display(ship_loss)
plt.figure(figsize=[6,6])
ship_loss.plot(kind='bar')''')

# Grouping by 'Ship_Mode' and counting the occurrences
ship_loss = df2.groupby('Ship_Mode')['Ship_Mode'].value_counts()

# Displaying the grouped data
st.write(ship_loss)

# Creating a figure with a specific size
fig, ax = plt.subplots(figsize=(6, 6))

# Creating the bar plot
ship_loss.plot(kind='bar', ax=ax)

# Setting the title and axis labels
plt.title('Distribution of Ship Modes')
plt.xlabel('Ship Mode')
plt.ylabel('Count')

# Displaying the plot in Streamlit
st.pyplot(fig)
'\n'
st.markdown('<hr>', unsafe_allow_html=True)


st.write('''# Conclusion :

## Recommendation base on insights from analysis:

Base on the analysis, what is best suit for the business manager to take as decisions to improve weak areas are:


1. Discount does not improve sales: The data indicates that offering discounts does not have a significant impact on increasing sales. This suggests that the company should explore other strategies to boost sales rather than relying solely on discounts.

2. Decent number of stores recorded loss: A considerable number of stores in different regions and categories experienced losses. This highlights the need for the company to address the underlying factors contributing to these losses and take appropriate measures to improve profitability.

3. No strong correlation between quantity of purchase and gain/loss: The analysis suggests that there is no strong correlation between the quantity of products purchased and the resulting gain or loss. This indicates that other factors, such as pricing, customer preferences, or market conditions, might have a more significant influence on sales performance.

4. Discount does not drive increased product purchases: The data shows that offering discounts does not necessarily lead to higher product purchases. This implies that customers may not be motivated solely by discounts and that other factors, such as product quality, customer service, or brand reputation, could play a more significant role in driving sales.

5. Sales distribution by category: The analysis reveals that office supplies were the most sold category, followed by furniture and technology. This information can be used to focus marketing efforts or inventory management strategies on the more popular categories.

6. Segment analysis: The consumer segment appears to be the most frequent patronizer, followed by the corporate and home office segments. This insight can help tailor marketing and customer service approaches to cater to the specific needs and preferences of each segment.

7. Top states with high losses: Several states, such as Texas, Ohio, Pennsylvania, and Illinois, recorded significant losses. This highlights the need to investigate and address the underlying reasons for these losses in each state.

Based on these findings, here are some recommendations:

- Continue to offer discounts, but be more strategic about when and how they are used.
- Review pricing strategies: Instead of relying solely on discounts, consider adjusting product prices based on market demand, competition, and profitability analysis.
- Focus on improving store profitability: Identify the reasons behind the losses in stores and regions and implement strategies to address those issues. This could involve optimizing inventory management, reducing operational costs, and exploring new marketing techniques.
- Customer-centric approach: Instead of solely relying on discounts to drive sales, focus on enhancing the overall customer experience. This could include improving product quality, providing excellent customer service, and creating loyalty programs to encourage repeat purchases.
- Market research: Conduct further market research to understand customer preferences, trends, and demands in different regions. This will help in tailoring marketing strategies and product offerings to better meet the needs of specific customer segments.
- Optimize inventory management: Analyze inventory levels and sales data to identify any discrepancies or areas where improvements can be made. Implementing a robust inventory tracking system can help reduce losses due to theft or mismanagement.
- Strengthen loss prevention practices: Implement loss prevention policies and train employees on best practices to prevent losses, such as theft or damage. Consider installing security cameras in high-traffic areas and collaborate with law enforcement if necessary.

By addressing these recommendations, the company can improve its sales performance, reduce losses, and enhance overall profitability. ''')


# Display a horizontal line
st.markdown('<hr>', unsafe_allow_html=True)

# Display a hyperlink to GitHub
link = '[GitHub](https://github.com/Barde-S)'
st.markdown(link, unsafe_allow_html=True)

link = '[Twitter](https://twitter.com/S_Barde74)'
st.markdown(link, unsafe_allow_html=True)

link = '[LinkedIn](https://www.linkedin.com/in/shuaibu-sani-barde-21b835227)'
st.markdown(link, unsafe_allow_html=True)

link = '[YouTube](https://www.youtube.com/@shuaibubarde249/)'
st.markdown(link, unsafe_allow_html=True)

# Display a horizontal line
st.markdown('<hr>', unsafe_allow_html=True)
st.write('<p style="text-align: right;">Shuaibu Sani Barde</p>', unsafe_allow_html=True)













