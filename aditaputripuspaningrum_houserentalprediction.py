# -*- coding: utf-8 -*-
"""AditaPutriPuspaningrum_HouseRentalPrediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16MzRgBp7hj815BHwwDIrdZFMLHhKLyCE

# Proyek Machine Learning Terapan (MLT4) - Submission 1 Predictive Analytics

*   Nama : Adita Putri Puspaningrum
*   Link Dataset : https://www.kaggle.com/datasets/iamsouravbanerjee/house-rent-prediction-dataset

# Data Collection
"""

# Commented out IPython magic to ensure Python compatibility.
# Import Libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# %matplotlib inline
import seaborn as sns

# Load the dataset
!gdown --id "11vCKuk81QvTQcwibMX7Wo6k4q0HDzLOz"

df = pd.read_csv("/content/House_Rent_Dataset.csv")
df.head()

"""# Check the Null Values"""

df.isnull().sum()

df.duplicated().sum()

"""# Exploratory Data Analysis (EDA)"""

df.info()
df.shape

df.describe()

sns.boxplot(x=df['BHK'])

sns.boxplot(x=df['Size'])

sns.boxplot(x=df['Bathroom'])

"""# Remove Outlier"""

# Drop kolom Posted On, Floor, Area Locality dan Point of Contact karena tidak mempengaruhi harga sewa
df = df.drop(['Posted On', 'Floor', 'Area Locality'], axis = 'columns')

df.groupby('City')['City'].agg('count')

df.groupby('Furnishing Status')['Furnishing Status'].agg('count')

df.groupby('Tenant Preferred')['Tenant Preferred'].agg('count')

df.groupby('Area Type')['Area Type'].agg('count')

df.groupby('Point of Contact')['Point of Contact'].agg('count')

# Fitur Area Type hanya memiliki 2 sample Built Area, karena data ini sangat kecil maka sample Built Area tersebut akan dihapus
df.drop(df.index[df['Area Type'] == 'Built Area'], inplace = True)

# Fitur Point of Contact hanya memiliki 1 sample Contact Builder, karena data ini sangat kecil maka sample Contact Builder tersebut akan dihapus
df.drop(df.index[df['Point of Contact'] == 'Contact Builder'], inplace = True)

Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
df = df[~((df<(Q1 - 1.5 * IQR)) | (df>(Q3 + 1.5 * IQR))).any(axis = 1)]

# Cek ukuran dataset setelah kita drop outliers
df.shape

df.head()

df.hist(bins=50, figsize=(10,5))
plt.show()

# Melihat kolerasi antara fitur kategorik dengan fitur target (Rent)
cat_features = df.select_dtypes(include='object').columns.to_list()

for col in cat_features:
  sns.catplot(x=col, y="Rent", kind="bar", dodge=False, height = 4, aspect = 3,  data=df, palette="Set3")
  plt.title("Rata-rata 'Rent' Relatif terhadap - {}".format(col))

# Mengamati hubungan antar fitur numerik dengan fungsi pairplot()
sns.pairplot(df, diag_kind = 'kde')

plt.figure(figsize=(10, 8))
correlation_matrix = df.corr().round(2)

sns.heatmap(data=correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5, )
plt.title("Correlation Matrix untuk Fitur Numerik ", size=20)

"""## One hot encoding"""

from sklearn.preprocessing import OneHotEncoder

df = pd.concat([df, pd.get_dummies(df['Area Type'], prefix='area_type')], axis=1)
df = pd.concat([df, pd.get_dummies(df['City'], prefix='city')], axis=1)
df = pd.concat([df, pd.get_dummies(df['Furnishing Status'], prefix='furnishing_status')], axis=1)
df = pd.concat([df, pd.get_dummies(df['Tenant Preferred'], prefix='tenant_preferred')], axis=1)
df = pd.concat([df, pd.get_dummies(df['Point of Contact'], prefix='point_of_contact')], axis=1)

df.drop(['Area Type', 'City', 'Furnishing Status', 'Tenant Preferred', 'Point of Contact'], axis=1, inplace=True)
df.head()

"""## Train Test Split"""

from sklearn.model_selection import train_test_split

X = df.drop(["Rent"],axis =1)
y = df["Rent"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.15)

print(f'Total # of sample in whole dataset: {len(X)}')
print(f'Total # of sample in train dataset: {len(X_train)}')
print(f'Total # of sample in test dataset: {len(X_test)}')

"""## Normalization"""

from sklearn.preprocessing import StandardScaler

# Normalisasi data train
numerical_features = ['BHK', 'Size', 'Bathroom']
scaler = StandardScaler()
scaler.fit(X_train[numerical_features])
X_train[numerical_features] = scaler.transform(X_train.loc[:, numerical_features])
X_train[numerical_features].head()

X_train[numerical_features].describe().round(4)

# Lakukan scaling terhadap fitur numerik pada X_test sehingga memiliki rata-rata=0 dan varians=1
X_test.loc[:, numerical_features] = scaler.transform(X_test[numerical_features])

"""# Modeling"""

from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import AdaBoostRegressor

from sklearn.metrics import mean_squared_error

# Siapkan dataframe untuk analisis model
models = pd.DataFrame(index=['train_mse', 'test_mse'],
                      columns=['knn', 'rf', 'boosting'])

knn = KNeighborsRegressor(n_neighbors = 14)
knn.fit(X_train, y_train)
models.loc['train_mse', 'knn'] = knn.score(X_test,y_test)
knn.score(X_test,y_test)

rf = RandomForestRegressor(n_estimators=50, max_depth=10, random_state=40, n_jobs=-1)
rf.fit(X_train, y_train)
models.loc['train_mse', 'rf'] = rf.score(X_test,y_test)
rf.score(X_test,y_test)

boosting = AdaBoostRegressor(n_estimators = 40, learning_rate = 0.05, random_state = 5)
boosting.fit(X_train, y_train)
models.loc['train_mse', 'boosting'] = boosting.score(X_test,y_test)
boosting.score(X_test,y_test)

"""# Evaluation"""

# Akurasi dari model
models

# Mean squared error dari model
mse = pd.DataFrame(columns=['train', 'test'], index=['KNN','RF','Boosting'])

model_dict = {'KNN': knn, 'RF': rf, 'Boosting': boosting}

for name, model in model_dict.items():
    mse.loc[name, 'train'] = mean_squared_error(y_true=y_train, y_pred=model.predict(X_train))/1e3
    mse.loc[name, 'test'] = mean_squared_error(y_true=y_test, y_pred=model.predict(X_test))/1e3

mse

fig, ax = plt.subplots()
mse.sort_values(by='test', ascending=False).plot(kind='barh', ax=ax, zorder=3)
ax.grid(zorder=0)

prediksi = X_test.iloc[:1].copy()
pred_dict = {'y_true':y_test[:1]}
for name, model in model_dict.items():
    pred_dict['prediksi_'+name] = model.predict(prediksi).round(1)

pd.DataFrame(pred_dict)