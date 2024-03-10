from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

URL ="resources/advices.txt"

# parse the advices from the file
def retrieve_advices():
    with open(URL) as file:
        return {line.strip(): 0 for line in file.readlines()}
            
advices = retrieve_advices()

# Choose a random advice, with a bias towards the least chosen advice
def get_rand_advice(advices):

    # Calculate the weights inversely proportional to count.
    weights = [1/(count+1) for count in advices.values()] 
    total = sum(weights) 
    weights = [weight / total for weight in weights]  # Normalise the weights
    
    advice = random.choices(list(advices.keys()), weights=weights)[0]
    advices[advice] += 1  # Increment the count for this advice
    return advice

        
@app.route("/")
def index():
    message = "Tip #" + str(gen_rand_number())
    # load_cpu()
    advice = get_rand_advice(advices)
    return render_template("index.html",message=message,advice=advice)

@app.route("/get_advice")
def get_advice():
    advice = get_rand_advice(advices)
    number = random.randint(1,876)
    return jsonify({"advice": advice, "number": number})

def load_cpu():
    for i in range(1000000):
        i * i

@app.route("/get_number")
def gen_rand_number():
    number = random.randint(1,876)
    return jsonify({"number":number})
    
app.run(host="0.0.0.0", port=5000,debug="true")