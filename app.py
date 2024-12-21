from flask import Flask, render_template
from bots import tf15,tf1,tf5
from analytics import c3tf15,c3tf30,c3tf1
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home/home.html")
@app.route("/tf15")
def bot1_index():
    msgs = tf15.get_signals()
    return render_template('bots/tf15.html', msgs=msgs)
@app.route("/tf5")
def bot2_index():
    msgs = tf5.get_signals()
    return render_template('bots/tf5.html', msgs=msgs)

@app.route("/tf1")
def bot3_index():
    msgs = tf1.get_signals()
    return render_template('bots/tf1.html', msgs=msgs)
@app.route("/c3tf15")
def ana1():
    results = c3tf15.get_results()
    return render_template("analytics/c3tf15.html", results=results)
@app.route("/c3tf30")
def ana2():
    results = c3tf30.get_results()
    return render_template("analytics/c3tf15.html", results=results)
@app.route("/c3tf1")
def ana3():
    results = c3tf1.get_results()
    return render_template("analytics/c3tf15.html", results=results)
@app.route("/blog")
def blog2():
    return render_template("blogs/blog.html")
@app.route("/voice")
def voiceass():
    return render_template("voiceass/voice.html")

if __name__ == "__main__":
   app.run(host='0.0.0.0',debug=True)