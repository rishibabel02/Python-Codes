import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {'Name': ['alice' , 'bob' , 'rishi' , 'yash'], "age":[25,30,20,19], 'city':['new york','london','bhl','pune']}

df = pd.DataFrame(data)
print(df)
# df['age'] = pd.to_numeric(df['age'] , errors='coerce')

#plotting a bar chart of name and age 
plt.bar(df['Name'] , df['age'])
plt.xlabel('Name')
plt.ylabel('Age')
plt.title('Age Dist: ')
plt.show()


#scatter plot for name and age 
sns.scatterplot(data = data , x = 'Name' , y = 'age')
plt.title('Scatter plot: name vs age')
plt.xlabel('Name')
plt.ylabel('Age')
plt.show()


