import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account

def load_data(df_table):
    """
    Loads data from Google BigQuery
    """
    key_path = "conf/GBQ.json"
    credentials = service_account.Credentials.from_service_account_file(key_path)

    try:
        df_table.to_gbq(credentials = credentials,
                        destination_table = 'neural-foundry-391916.dataset_steamdb.table-sales',
                        if_exists = 'replace')
        print("ETL job successful!")
    except:
        print("ETL job failed!")