def clean_data(df):
    """
    Clean the bank customer churn dataset.
    """

    df = df.copy()

    df = df.drop(
        columns=[
            "RowNumber",
            "CustomerId",
            "Surname"
        ]
    )

    df = df.rename(columns={
        "CreditScore": "Credit Score",
        "NumOfProducts": "Number of Products",
        "HasCrCard": "Has Credit Card",
        "IsActiveMember": "Active Member",
        "EstimatedSalary": "Estimated Salary",
        "Exited": "Churn"
    })

    return df