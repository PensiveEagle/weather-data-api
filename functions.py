from datetime import datetime
import pandas as pd
import json
from dateutil.parser import parse as date_parse

def extract_data( data_filepath: str, skip_rows: int = 20 ) -> pd.DataFrame:
    df = pd.read_csv( data_filepath, skiprows = skip_rows )
    df.columns = [col.strip() for col in df.columns]
    return df

def filter_dataframe_on_date( dataframe: pd.DataFrame, filter_date: datetime ) -> pd.DataFrame:
    dataframe["DATE"] = pd.to_datetime( dataframe["DATE"], format = "ISO8601" )
    dataframe = dataframe[dataframe["DATE"] == filter_date]
    return dataframe

def filter_dataframe_on_year( dataframe: pd.DataFrame, filter_year: int ) -> pd.DataFrame:
    dataframe["DATE"] = dataframe["DATE"].astype(str)
    dataframe = dataframe[dataframe["DATE"].str.startswith(str(filter_year))]
    return dataframe

def dataframe_to_json( dataframe: pd.DataFrame ) -> dict:
    dataframe["DATE"] = pd.to_datetime( dataframe["DATE"], format = "ISO8601" )
    json_string = dataframe.to_json( orient = "table", index = False )
    return json.loads( json_string )