import pandas as pd
df= pd.read_csv("restaurant_orders.csv")

import matplotlib.pyplot as plt


#1)revenue column:

df['Revenue']=df['Price']*df['Quantity']

#2) MOST ORDERED FOOD ITEM:
moi= df.groupby('Food Item')['Quantity'].sum().sort_values(ascending=False)
print('MOST ORDERED ITEM :',moi)
print()


#3) CATEGORY WISE SALES (I):
cs=df.groupby('Food Item')['Revenue'].sum().sort_values(ascending=False)
print('CATEGORY WISE SALES (I) :',cs)
print()

#)CARTEGORY WISE SALES (II):
cws=df.groupby('Category')['Revenue'].sum().sort_values(ascending=False)
print('CATEGORY WISE SALES (II) :',cws)
print()

#4)PEAKED ORDER TIME:

#) for changing the time into morning/afternoon/evening:

df['Order Time']=pd.to_datetime(df['Order Time'])
df['hour']=df['Order Time'].dt.hour
df['time_period']=df['hour'].apply(lambda x:
                                   'morning' if 6 <= x < 12 else
                                   'afternoon' if 12 <= x < 18 else
                                   'evening')
    
pot=df['time_period'].value_counts().sort_values(ascending=False)
print('PEAK ORDER TIME :',pot)
print()

#5) TOP REVENUE FOOD ITEM :
tri=df.groupby('Food Item')['Revenue'].sum().sort_values(ascending=False)
print('TOP REVENUE FOOD ITEM :',tri)
print()


# CHARTS:
#1) MOST ORDERED FOOD ITEM:

moi.plot(kind='bar', color='skyblue')
plt.title('MOST ORDERED FOOD ITEM')
plt.xlabel('FOOD ITEM')
plt.ylabel('QUANTITY')
plt.savefig("output\most ordered_food_item_chart.png")
plt.show()

#2) CATEGORY WISE SALES (I):

cs.plot(kind='bar',color='red')
plt.title('CATEGORY WISE SALES(I)')
plt.xlabel('FOOD ITEM ')
plt.ylabel('REVENUE')
plt.savefig("output\category_wise_sales(i)_chart.png")
plt.show()


#) CATEGORY WISE SALES (II):

cws.plot(kind='pie',autopct='%1.F%%',startangle=90,color=['green','red','yellow'])
plt.title('CATEEGORY WISE SALES(II)')
plt.xlabel('CATEGORY')
plt.legend()
plt.savefig("output\category_wise_sales(ii)_chart.png")
plt.show()

#3) PEAKED ORDER TIME:

pot.plot(kind='pie',autopct='%1.1F%%',startangle=90,color=['light green','skyblue','pink'])
plt.title('PEAK ORDER TIME')
plt.legend()
plt.savefig("output\peak_order_time_chart.png")
plt.show()


#4) PRICE Vs QUANTITY:
ap=df.groupby('Quantity')['Price'].mean()

plt.bar(ap.index,ap.values,color='purple')
plt.title('AVERAGE PRICE BY QUANTITY')
plt.xlabel('QUANTITY')
plt.ylabel('AVERAGE PRICE')
plt.savefig("output/average_price_chart.png")
plt.show()

























