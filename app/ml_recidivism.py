import matplotlib.pyplot as plt
import pandas as pd
from .K_neighbors_classifier import  KNeighborsClassifier
import random


class GetDataVisualizations:

    def convicting_offense(self, data):

        plt.figure(figsize=(10, 10))
        plt.subplot(1, 2, 1)  # row 1, col 2 index 1
        data['Race - Ethnicity'].value_counts().plot(kind='bar')
        plt.title("Race - Ethnicity")
        plt.ylabel('Count')

        plt.subplot(1, 2, 2)  # index 2
        data['Convicting Offense Classification'].value_counts().plot(kind='bar')
        plt.title("Convicting Offense Classification")

        plt.show()

    def age_at_release(self, data):

        plt.figure(figsize=(10, 10))
        plt.subplot(1, 2, 1)  # row 1, col 2 index 1
        data['Recidivism - Return to Prison numeric'].value_counts().plot(kind='bar')
        plt.title("Recidivism - Return to Prison numeric")
        plt.ylabel('Count')

        plt.subplot(1, 2, 2)  # index 2
        data['Age At Release '].value_counts().plot(kind='bar')
        plt.title("Age At Release ")

        plt.show()

    def who_didnt_return(self, data):

        plt.figure(figsize=(10, 10))
        plt.subplot(1, 2, 1)  # row 1, col 2 index 1
        data.loc[data['Recidivism - Return to Prison numeric'] == 1]['Age At Release '].value_counts().plot(kind='bar')
        plt.title("Age at release of people who returned to prison")
        plt.ylabel('Count')

        plt.subplot(1, 2, 2)  # index 2
        data.loc[data['Recidivism - Return to Prison numeric'] == 0]['Age At Release '].value_counts().plot(kind='bar')
        plt.title("Age at release of people who didn't return")

        plt.show()

    def algo_accuracy(self, ):
        url = "https://raw.githubusercontent.com/adebayoj/fairml/master/doc/example_notebooks/propublica_data_for_fairml.csv"
        data2 = pd.read_csv(url)
        X = data2.drop(["Two_yr_Recidivism"], axis=1)
        y = data2["Two_yr_Recidivism"]

        # Spliting the data into train and test data.
        number_of_rows = len(y)
        all_rows = range(0, number_of_rows)
        percentage_train = 0.8
        train_len = round(number_of_rows * percentage_train)
        training_rows = random.sample(all_rows, train_len)

        testing_rows = []

        for i in range(number_of_rows):
            if i not in training_rows:
                testing_rows.append(i)

        X_train = X.iloc[training_rows]
        y_train = y.iloc[training_rows]
        X_test = X.iloc[testing_rows]
        y_test = y.iloc[testing_rows]

        # Turning pandas df to numpy array. Numpy is really good at doing calculations quickly.
        X_train = X_train.to_numpy()
        y_train = y_train.to_numpy()

        X_test = X_test.to_numpy()
        y_test = y_test.to_numpy()

        X_train2 = X_train[0:10000]
        y_train2 = y_train[0:10000]

        X_test2 = X_test[0:2000]
        y_test2 = y_test[0:2000]

        number_of_rows = len(y)
        all_rows = range(0, number_of_rows)
        percentage_train = 0.8
        train_len = round(number_of_rows * percentage_train)
        training_rows = random.sample(all_rows, train_len)

        # Test knn model across varying ks
        list_of_accuracies = []
        ks = range(1, 35)
        for k in ks:
            # Create a classifier for each k
            knn = KNeighborsClassifier(k=k)

            # Fit the model using the training data.
            knn.fit(X_train2, y_train2)

            # Test the moddel using the testing data, and get the accuracy
            accuracy = knn.evaluate(X_test2, y_test2)

            # Append the accuracy to the list so we can later plot it.
            list_of_accuracies.append(accuracy)
        # Visualize accuracy vs. k
        fig, ax = plt.subplots()
        ax.plot(ks, list_of_accuracies)
        ax.set(xlabel="k",
               ylabel="Accuracy",
               title="Algorithm performance with second dataset")
        plt.show()


class GetImageDataVisualizations:

    def convicting_offense(self, data):

        plt.figure(figsize=(10, 10))
        plt.subplot(1, 2, 1)  # row 1, col 2 index 1
        data['Race - Ethnicity'].value_counts().plot(kind='bar')
        plt.title("Race - Ethnicity")
        plt.ylabel('Count')

        plt.subplot(1, 2, 2)  # index 2
        data['Convicting Offense Classification'].value_counts().plot(kind='bar')
        plt.title("Convicting Offense Classification")

        plt.savefig("app/static/plot1.png")

    def age_at_release(self, data):

        plt.figure(figsize=(10, 10))
        plt.subplot(1, 2, 1)  # row 1, col 2 index 1
        data['Recidivism - Return to Prison numeric'].value_counts().plot(kind='bar')
        plt.title("Recidivism - Return to Prison numeric")
        plt.ylabel('Count')

        plt.subplot(1, 2, 2)
        data['Age At Release '].value_counts().plot(kind='bar')
        plt.title("Age At Release ")
        plt.savefig("app/static/plot2.png")

    def who_didnt_return(self, data):
        # Seeing if there is a correlation between age and recidivism
        plt.figure(figsize=(10, 10))
        plt.subplot(1, 2, 1)
        data.loc[data['Recidivism - Return to Prison numeric'] == 1]['Age At Release '].value_counts().plot(kind='bar')
        plt.title("Age at release of people who returned to prison")
        plt.ylabel('Count')

        plt.subplot(1, 2, 2)
        data.loc[data['Recidivism - Return to Prison numeric'] == 0]['Age At Release '].value_counts().plot(kind='bar')
        plt.title("Age at release of people who didn't return")

        plt.savefig("app/static/plot3.png")

    def algo_accuracy(self, ):

        url = "https://raw.githubusercontent.com/adebayoj/fairml/master/doc/example_notebooks/propublica_data_for_fairml.csv"
        data2 = pd.read_csv(url)
        X = data2.drop(["Two_yr_Recidivism"], axis=1)
        y = data2["Two_yr_Recidivism"]

        # Spliting the data into train and test data.
        number_of_rows = len(y)
        all_rows = range(0, number_of_rows)
        percentage_train = 0.8
        train_len = round(number_of_rows * percentage_train)
        training_rows = random.sample(all_rows, train_len)

        testing_rows = []

        for i in range(number_of_rows):
            if i not in training_rows:
                testing_rows.append(i)

        X_train = X.iloc[training_rows]
        y_train = y.iloc[training_rows]
        X_test = X.iloc[testing_rows]
        y_test = y.iloc[testing_rows]

        # Turning pandas df to numpy array. Numpy is really good at doing calculations quickly.
        X_train = X_train.to_numpy()
        y_train = y_train.to_numpy()

        X_test = X_test.to_numpy()
        y_test = y_test.to_numpy()

        X_train2 = X_train[0:10000]
        y_train2 = y_train[0:10000]

        X_test2 = X_test[0:2000]
        y_test2 = y_test[0:2000]

        number_of_rows = len(y)
        all_rows = range(0, number_of_rows)
        percentage_train = 0.8
        train_len = round(number_of_rows * percentage_train)
        training_rows = random.sample(all_rows, train_len)

        testing_rows = []

        for i in range(number_of_rows):
            if i not in training_rows:
                testing_rows.append(i)
        X_train = X.iloc[training_rows]
        y_train = y.iloc[training_rows]
        X_test = X.iloc[testing_rows]
        y_test = y.iloc[testing_rows]

        # Turning pandas df to numpy array. Numpy is really good at doing calculations quickly.
        X_train = X_train.to_numpy()
        y_train = y_train.to_numpy()
        X_test = X_test.to_numpy()
        y_test = y_test.to_numpy()

        # Test knn model across varying ks
        list_of_accuracies = []
        ks = range(1, 35)
        for k in ks:
            # Create a classifier for each k
            knn = KNeighborsClassifier(k=k)

            # Fit the model using the training data.
            knn.fit(X_train2, y_train2)

            # Test the moddel using the testing data, and get the accuracy
            accuracy = knn.evaluate(X_test2, y_test2)

            # Append the accuracy to the list so we can later plot it.
            list_of_accuracies.append(accuracy)
        # Visualize accuracy vs. k
        fig, ax = plt.subplots()
        ax.plot(ks, list_of_accuracies)
        ax.set(xlabel="k",
               ylabel="Accuracy",
               title="Algorithm performance with second dataset")
        print("Working ")
        plt.savefig("app/static/plot4.png")

