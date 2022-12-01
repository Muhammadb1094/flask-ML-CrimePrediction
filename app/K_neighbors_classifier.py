import numpy as np

def most_common(vote_list):
  return max(set(vote_list), key=vote_list.count)


# Calculating the euclidian distance between the point and the data.
def euclidean(point, data):
  return np.sqrt(np.sum((point - data) ** 2, axis=1))



class KNeighborsClassifier:

  # Initializing with k, and with the distance function
  def __init__(self, k=5, dist_metric=euclidean):
    self.k = k
    self.dist_metric = dist_metric

  def fit(self, X_train, y_train):
    self.X_train = X_train
    self.y_train = y_train

  def predict(self, X_test):
    neighbors = []
    for x in X_test:
        distances = self.dist_metric(x, self.X_train)
        y_sorted = [y for _, y in sorted(zip(distances, self.y_train))]
        neighbors.append(y_sorted[:self.k])

    return list(map(most_common, neighbors))


  def evaluate(self, X_test, y_test):
    # Predict using X_test then compare the predicted value with the real value
    y_pred = self.predict(X_test)

    # Accuracy will be equal to the number of correct guesses divided by total guesses.
    accuracy = sum(y_pred == y_test) / len(y_test)
    return accuracy