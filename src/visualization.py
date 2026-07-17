import matplotlib.pyplot as plt


def plot_churn_distribution(df):

    counts = df["Churn"].value_counts()

    plt.figure(figsize=(6,4))

    plt.bar(
        ["Stayed", "Left"],
        counts
    )

    plt.title("Customer Churn Distribution")

    plt.xlabel("Customer Status")

    plt.ylabel("Number of Customers")

    plt.show()