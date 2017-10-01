#import tensorflow.contrib.learn as skflow
from sklearn import datasets, metrics, svm

iris =datasets.load_iris()
classifier = svm.SVC(gamma=0.001)
classifier.fit(iris.data, iris.target)
score = metrics.accuracy_score(iris.target, classifier.predict(iris.data))
print("accuracy_score: " %score)




