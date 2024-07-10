import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    customers_wdp = customers.drop_duplicates(inplace=True)
    return customers_wdp
