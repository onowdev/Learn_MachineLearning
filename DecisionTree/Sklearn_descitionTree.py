import imp


import pandas as pd
from sklearn.datasets import load_iris

# membaca dataset Iris
iris = pd.read_csv('/home/onowdev/Documents/LESON/python/machineLearning/Learn_MachineLearning/DecisionTree/Iris_Data.csv')

# Melihat dataset Iris
iris.info()

# Melihat 5 dataset teratas

iris.head()

# menghilangkan kolom yang tidak penting
# iris.drop('Id',axis=1,inplace=True)

# memisahkan atribut dan Label
X = iris[['sepal_length','sepal_width','petal_length','petal_width']]
y = iris['species']

#Membagi dataset menjadi 2, Latih (Training) & Uji (testing)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train,y_test = train_test_split(X,y, test_size=0.1, random_state=123)

from sklearn.tree import DecisionTreeClassifier

#Membuat Model decision Tree
tree_model = DecisionTreeClassifier()

# Melatih Model dengan data Latih
tree_model = tree_model.fit(X_train, y_train)

# Evaluasi Model
from sklearn.metrics import accuracy_score

y_pred = tree_model.predict(X_test)

acc_score = round(accuracy_score(y_pred, y_test),3)

print('Accuracy:', acc_score)

# prediksi model dengan tree_model.predict([[SepalLength, SepalWidth, PetalLength, PetalWidth]])
print(tree_model.predict([[6.2, 3.4, 5.4, 2.3]])[0])

from sklearn.tree import export_graphviz
export_graphviz(
    tree_model,
    out_file = "iris_tree.dot",
    feature_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width'],
    class_names = ['Iris_setosa', 'Iris_versicolor' ,'Iris_virginica'],
    rounded = True,
    filled = True)