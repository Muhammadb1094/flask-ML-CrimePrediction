import matplotlib.pyplot as plt


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
