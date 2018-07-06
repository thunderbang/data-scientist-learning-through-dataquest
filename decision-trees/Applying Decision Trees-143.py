## 3. Splitting the Data into Train and Test Sets ##

import numpy
import math

# Set a random seed so the shuffle is the same every time
numpy.random.seed(1)

# Shuffle the rows  
# This permutes the index randomly using numpy.random.permutation
# Then, it reindexes the dataframe with the result
# The net effect is to put the rows into random order
income = income.reindex(numpy.random.permutation(income.index))

train_max_row = math.floor(income.shape[0] * .8)
train = income.iloc[:train_max_row]
test = income.iloc[train_max_row:]

## 4. Evaluating Error With AUC ##

from sklearn.metrics import roc_auc_score

clf = DecisionTreeClassifier(random_state=1)
clf.fit(train[columns], train["high_income"])

predictions = clf.predict(test[columns])
error = roc_auc_score(test["high_income"], predictions)
print(error)

## 5. Computing Error on the Training Set ##

predictions = clf.predict(train[columns])
print(roc_auc_score(train["high_income"], predictions))

## 7. Reducing Overfitting With a Shallower Tree ##

# Decision trees model from the last screen
clf = DecisionTreeClassifier(random_state=1)
clf = DecisionTreeClassifier(min_samples_split=13, random_state=1)
clf.fit(train[columns], train["high_income"])
predictions = clf.predict(test[columns])
test_auc = roc_auc_score(test["high_income"], predictions)

train_predictions = clf.predict(train[columns])
train_auc = roc_auc_score(train["high_income"], train_predictions)

print(test_auc)
print(train_auc)