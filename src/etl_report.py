from src.extract import extract_data
from src.load import load_data
from src.transform import transform_data, get_data

class Etl_report():
    def __init__(self) -> None:
        self

    def run_etl(self):
        source = extract_data()
        df_table = transform_data(get_data(source))
        load_data(df_table)