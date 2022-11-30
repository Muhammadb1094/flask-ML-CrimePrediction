import pandas as pd
import matplotlib.pyplot as plt


class GetDataVisualizations:

    def convicting_offense(self, data):
        # Plotting race and Convicting Offense Classification to understand the data more
        plt.figure(figsize=(10, 10))
        plt.subplot(1, 2, 1)  # row 1, col 2 index 1
        data['Race - Ethnicity'].value_counts().plot(kind='bar')
        plt.title("Race - Ethnicity")
        plt.ylabel('Count')

        plt.subplot(1, 2, 2)  # index 2
        data['Convicting Offense Classification'].value_counts().plot(kind='bar')
        plt.title("Convicting Offense Classification")
        # plt.show()
        image = plt.savefig('my_plot1.png')
        print(image)

    def age_at_release(self, data):
        # Plotting age and Recidivism
        plt.figure(figsize=(10, 10))
        plt.subplot(1, 2, 1)  # row 1, col 2 index 1
        data['Recidivism - Return to Prison numeric'].value_counts().plot(kind='bar')
        plt.title("Recidivism - Return to Prison numeric")
        plt.ylabel('Count')

        plt.subplot(1, 2, 2)  # index 2
        data['Age At Release '].value_counts().plot(kind='bar')
        plt.title("Age At Release ")
        # plt.show()

        image = plt.savefig('my_plot2.png')
        print(image)

    def who_didnt_return(self, data):
        # Seeing if there is a correlation between age and recidivism
        # plt.figure(figsize=(10, 10))
        # plt.subplot(1, 2, 1)  # row 1, col 2 index 1
        # data.loc[data['Recidivism - Return to Prison numeric'] == 1]['Age At Release '].value_counts().plot(kind='bar')
        # plt.title("Age at release of people who returned to prison")
        # plt.ylabel('Count')
        #
        # plt.subplot(1, 2, 2)  # index 2
        # data.loc[data['Recidivism - Return to Prison numeric'] == 0]['Age At Release '].value_counts().plot(kind='bar')
        # plt.title("Age at release of people who didn't return")
        # # plt.show()
        # image = plt.savefig('my_plot3.png')
        # print(image)
        # Cleaning up the data. Here we create new columns for categorical columns like Race, Age, Conviction Offense,
        # and Release type.
        # Machine learning algorithms prefer numbers as input.
        data_race = pd.get_dummies(data['Race - Ethnicity'])
        placeholder_data = pd.concat([data, data_race], axis=1)

        data_age = pd.get_dummies(placeholder_data['Age At Release '])
        placeholder_data = pd.concat([placeholder_data, data_age], axis=1)

        data_offese_clasification = pd.get_dummies(placeholder_data['Convicting Offense Classification'])
        placeholder_data = pd.concat([placeholder_data, data_offese_clasification], axis=1)

        data_release_type = pd.get_dummies(placeholder_data['Release Type'])
        placeholder_data = pd.concat([placeholder_data, data_release_type], axis=1)

        final_data = placeholder_data.drop(["Fiscal Year Released", "Recidivism Reporting Year", "Race - Ethnicity",
                                            "Age At Release ", "Convicting Offense Classification",
                                            "Convicting Offense Type", "Convicting Offense Subtype", "Release Type",
                                            "Release type: Paroled to Detainder united", "Main Supervising District",
                                            "N/A -", "Part of Target Population"], axis=1)

        # plt.plot(final_data)
        # plt.show()
        plt.plot(final_data)
        image = plt.savefig('my_plot4.png')
        print(image)
        # Spliting the data into input data (X), and output data (y).
        # The input variables will be the variables that, will be fed into the model and the output
        # variable will be the "Recidivism - Return to Prison numeric".
        X = data.drop(["Recidivism - Return to Prison numeric"], axis=1)
        y = data["Recidivism - Return to Prison numeric"]
        print("XXXXXXXXXX")
        print(X)
        print(y)
        print("YYYYYYYYYYYYYY")
        # plt.plot(X, y)
        # plt.show()