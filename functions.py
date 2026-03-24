from datetime import datetime
import pandas as pd
import json

def extract_data( data_filepath: str ) -> pd.DataFrame:
    df = pd.read_csv( data_filepath, skiprows = 20 )
    df.columns = [col.strip() for col in df.columns]
    df["DATE"] = pd.to_datetime( df["DATE"], format = "ISO8601" )
    return df

def filter_dataframe_on_date( dataframe: pd.DataFrame, filter_date: datetime ) -> pd.DataFrame:
    dataframe = dataframe[dataframe["DATE"] == filter_date]
    return dataframe

def dataframe_to_json( dataframe: pd.DataFrame ) -> dict:
    json_string = dataframe.to_json( orient = "table", index = False )
    return json.loads( json_string )