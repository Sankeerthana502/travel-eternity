from flask import Flask, render_template, request

app = Flask(__name__)


def generate_itinerary(days):

    plans = [

        "Visit Yadadri Temple and attend morning pooja",

        "Explore nearby spiritual places and local food",

        "Evening relaxation and photography spots"
    ]

    itinerary = []

    for i in range(days):

        plan = plans[i % len(plans)]

        itinerary.append(
            f"Day {i+1}: {plan}"
        )

    return itinerary


@app.route('/')
def home():

    return render_template('index.html')


@app.route('/plan', methods=['POST'])
def plan():

    username = request.form['username']

    email = request.form['email']

    destination = request.form['destination']

    interest = request.form['interest']

    travel_type = request.form['travel_type']

    budget = request.form['budget']

    days = int(request.form['days'])

    itinerary = generate_itinerary(days)

    accommodation = (
        "Budget-friendly lodge near Yadadri Temple"
    )

    return render_template(

        'result.html',

        username=username,

        email=email,

        destination=destination,

        interest=interest,

        travel_type=travel_type,

        budget=budget,

        days=days,

        itinerary=itinerary,

        accommodation=accommodation
    )


if __name__ == '__main__':

    app.run(debug=True)