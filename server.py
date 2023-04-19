from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.errorhandler(404) 
def handle_error(error):
    res="<script>alert('Sorry! No response. Try again.')</script>"
    return res

@app.route('/play')          # The "@" decorator associates this route with the function immediately following
def play():
    return render_template("index.html", num=3,col="#9FC5F8")
    
@app.route('/play/<int:times>')          # The "@" decorator associates this route with the function immediately following
def play_times(times):
    return render_template("index.html", num=times,col="#9FC5F8")

@app.route('/play/<int:times>/<string:color>')          # The "@" decorator associates this route with the function immediately following
def play_times_colors(times,color):
    return render_template("index.html", num=times, col=color)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
