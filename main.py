from flask import Flask, render_template

app = Flask( __name__ )

@app.route( "/" )
def home():
    return render_template("home.html")

@app.route( "/api/v1/<station_id>/<date>" )
def about(station_id, date):
    return {"station": station_id,
            "date": date,
            "temperature": "holding"}

if __name__ == "__main__":
    app.run(debug=True)