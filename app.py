from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection 
# mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")
app.config['MONGO_URI'] = "mongodb://localhost:27017/marsData_db"
mongo = PyMongo(app)

# Route to render index.html template using data from Mongo
@app.route("/")
def index():
    mars_data = mongo.db.marsData.find_one()
    return render_template("index.html", mars_data=mars_data)
    


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():
    
    #run scrape function
    mars_data = scrape_mars.scrape_info()
    
    #update the Mongo database
    mongo.db.marsData.update({}, mars_data, upsert=True)

    #redirect back to homepage
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)