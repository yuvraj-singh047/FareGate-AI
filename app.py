from flask import Flask, render_template, request
import pickle, pandas as pd
from datetime import timedelta

app = Flask(__name__, template_folder='./templates', static_folder='./static')

model = pickle.load(open('./models/model.pkl', 'rb'))
preprocessor = pickle.load(open('./models/preprocessor.pkl', 'rb'))


AIRLINES = [
    'IndiGo', 'Air India', 'Jet Airways', 'SpiceJet', 'Multiple carriers',
    'GoAir', 'Vistara', 'Air Asia', 'Vistara Premium economy',
    'Jet Airways Business', 'Multiple carriers Premium economy', 'Trujet'
]
CITIES = ['Banglore', 'Kolkata', 'Delhi', 'Mumbai', 'Chennai', 'New Delhi', 'Cochin', 'Hyderabad']
ADDITIONAL_INFO = ['No Info', 'In-flight meal not included', 'No check-in baggage included', 'Other']
STOPS = [0, 1, 2, 3, 4]


@app.route("/", methods=['GET', 'POST'])
def predict():
    prediction = None
    error = None
    Duration_Hour = None
    Duration_Minute = None

    if request.method == 'POST':
        try:
            Airline = request.form['airline']
            Source = request.form['source']
            Destination = request.form['destination']
            Total_Stops = int(request.form['stops'])
            Additional_Info = request.form['additional_info']

            if Source == Destination:
                raise ValueError("Source and destination can't be the same city.")


            flight_date = pd.to_datetime(request.form['date'])
            Date = flight_date.day
            Month = flight_date.month
            Year = flight_date.year

            dep_time = pd.to_datetime(request.form['dep_time'])
            Dep_Hour = dep_time.hour
            Dep_Min = dep_time.minute

            arr_time = pd.to_datetime(request.form['arr_time'])
            Arrival_Hour = arr_time.hour
            Arrival_Minute = arr_time.minute

            if arr_time <= dep_time:
                arr_time += timedelta(days=1)
            duration = arr_time - dep_time
            Duration_Hour = duration.seconds // 3600
            Duration_Minute = (duration.seconds % 3600) // 60

            data = pd.DataFrame([{
                'Airline': Airline,
                'Source': Source,
                'Destination': Destination,
                'Total_Stops': Total_Stops,
                'Additional_Info': Additional_Info,
                'Date': Date,
                'Month': Month,
                'Year': Year,
                'Dep_Hour': Dep_Hour,
                'Dep_Min': Dep_Min,
                'Arrival_Hour': Arrival_Hour,
                'Arrival_Minute': Arrival_Minute,
                'Duration_Hour': Duration_Hour,
                'Duration_Minute': Duration_Minute
            }])

            data = preprocessor.transform(data)
            prediction = round(float(model.predict(data)[0]))

        except Exception as e:
            error = str(e)

    return render_template(
        'index.html',
        airlines=AIRLINES,
        cities=CITIES,
        additional_info=ADDITIONAL_INFO,
        stops=STOPS,
        prediction=prediction,
        duration_hour=Duration_Hour,
        duration_minute=Duration_Minute,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)