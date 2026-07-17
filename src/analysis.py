def churn_rate(df):
    """
    Return the customer churn percentage.
    """

    return (
        df["Churn"]
        .value_counts(normalize=True)
        * 100
    ).round(2)


def average_age(df):
    """
    Return average age grouped by churn.
    """

    return df.groupby("Churn")["Age"].mean()