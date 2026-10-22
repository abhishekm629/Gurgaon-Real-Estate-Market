import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('realestate_data.csv')


# data cleaning

df.columns = df.columns.str.strip().str.lower().str.replace(' ','_')
df.columns = df.columns.str.replace('socity','society')
df.columns = df.columns


# data cleaning

df["price"] = df["price"].astype(str).str.replace(",","").astype(float)
df["area"] = df["area"].astype(str).str.replace("," , "").astype(int)

df["rate_per_sqft"] = (
    df["rate_per_sqft"]
    .astype(str)
    .str.replace("'", "", regex=False)  
    .str.replace(",", "", regex=False)  
    .str.strip()                    
    .astype(int)                   
)

# categorical columns cleaning
df['status'] = df['status'].str.strip().str.lower()
df['rera_approval'] = df['rera_approval'].str.strip().str.lower().map({'approved by rera' : True , 'not approved by rera':False})

df['flat_type'] = df["flat_type"].str.strip().str.lower()

df = df.drop_duplicates()

# Question 1: Which is the costliest flat?

costliest_flat = df.loc[df['price'].idxmax()]
print("Costliest flat:")
print(costliest_flat.to_string())

#  Which locality has the highest average price?

highest_avg_price = df.groupby('locality')['price'].mean().idxmax()
print(f"Locality with the highest average price: {highest_avg_price}")


#  Which locality has the highest rate per square foot?

highest_rate_per_sqft = df.groupby('locality')['rate_per_sqft'].mean().idxmax()
print(f"Locality with the highest average rate per sq. ft.: {highest_rate_per_sqft}")

# do Ready-to-move properties cost more than Under-construction properties.
ready_to_move_avg_price = df[df['status'] == 'ready to move']['price'].mean()
under_construction_avg_price = df[df['status'] == 'under construction']['price'].mean()

if ready_to_move_avg_price > under_construction_avg_price:
    comparison = "Ready-to-move properties cost more on average."
elif ready_to_move_avg_price < under_construction_avg_price:
    comparison = "Under-construction properties cost more on average."
else:
    comparison = "Both property statuses have the same average price."
print(
    f"{comparison} "
    f"Ready-to-move: {ready_to_move_avg_price:,.2f}; "
    f"under construction: {under_construction_avg_price:,.2f}."
)

#  Does RERA approval affect pricing?
rera_approved_avg_price = df[df['rera_approval'] == True]['price'].mean()
rera_not_approved_avg_price = df[df['rera_approval'] == False]['price'].mean()

if rera_approved_avg_price > rera_not_approved_avg_price:
    comparison = "RERA-approved properties have a higher average price."
elif rera_approved_avg_price < rera_not_approved_avg_price:
    comparison = "RERA-approved properties have a lower average price."
else:
    comparison = "RERA-approved and non-approved properties have the same average price."
print(
    f"{comparison} "
    f"Approved: {rera_approved_avg_price:,.2f}; "
    f"not approved: {rera_not_approved_avg_price:,.2f}."
)

# How does area impact price?
sns.scatterplot(data = df , x = 'area' , y = 'price')
plt.title('area vs price')
plt.show()

# Which BHK configuration is most expensive based on per sqft area?
most_expensive_bhk = df.groupby('bhk_count')['rate_per_sqft'].mean().idxmax()
print(f"BHK configuration with the highest average rate per sq. ft.: {most_expensive_bhk}")


# Which property type is the costliest?
most_expensive_property_type = df.groupby('flat_type')['rate_per_sqft'].mean().idxmax()
print(f"Property type with the highest average rate per sq. ft.: {most_expensive_property_type}")


#  Do certain builders price higher?
# top 5 builders

top_5_builders = df.groupby('company_name')['rate_per_sqft'].mean().sort_values(ascending=False).head(5)
print("Top 5 builders by average rate per sq. ft.:")
print(top_5_builders.to_string(float_format=lambda value: f"{value:,.2f}"))



#  Are larger homes more expensive per sqft?

sns.scatterplot(data = df , x = 'area' , y = 'rate_per_sqft')
plt.show()
