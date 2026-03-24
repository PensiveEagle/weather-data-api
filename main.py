from flask import Flask, render_template
from functions import extract_data, filter_dataframe_on_date, filter_dataframe_on_year, dataframe_to_json
from dateutil.parser import parse as date_parse

app = Flask( __name__ )

stations = extract_data( "./data/stations.txt", skip_rows = 17 )[["STAID", "STANAME"]]


@app.route( "/" )
def home():
    return render_template( "home.html", stations_table=stations.to_html() )

@app.route( "/api/v1/full/<station_id>" )
def all_station_data(station_id):
    station_identifier = station_id.zfill( 6 )
    return dataframe_to_json( extract_data( f"./data/TG_STAID{station_identifier}.txt") )

@app.route( "/api/v1/single/<station_id>/<date>" )
def station_data(station_id, date):
    filter_date = date_parse( date )
    station_identifier = station_id.zfill( 6 )
    return dataframe_to_json( filter_dataframe_on_date( extract_data( f"./data/TG_STAID{station_identifier}.txt"), filter_date ) )

@app.route( "/api/v1/yearly/<station_id>/<year>" )
def year_station_data(station_id, year):
    station_identifier = station_id.zfill( 6 )
    return dataframe_to_json( filter_dataframe_on_year( extract_data( f"./data/TG_STAID{station_identifier}.txt"), year ) )


if __name__ == "__main__":
    app.run(debug = True, port = 5050)