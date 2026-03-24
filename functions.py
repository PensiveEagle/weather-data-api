from datetime import datetime
import pandas as pd
import json

def extract_data( data_filepath: str, skip_rows: int = 20, has_index: bool = True ) -> pd.DataFrame:
    df = pd.read_csv( data_filepath, skiprows = skip_rows )
    df.columns = [col.strip() for col in df.columns]
    return df

def filter_dataframe_on_date( dataframe: pd.DataFrame, filter_date: datetime ) -> pd.DataFrame:
    dataframe["DATE"] = pd.to_datetime( dataframe["DATE"], format = "ISO8601" )
    dataframe = dataframe[dataframe["DATE"] == filter_date]
    return dataframe

def dataframe_to_json( dataframe: pd.DataFrame ) -> dict:
    json_string = dataframe.to_json( orient = "table", index = False )
    return json.loads( json_string )