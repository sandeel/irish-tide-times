from flask import Flask, render_template, request, redirect
import twilio.twiml
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route("/receive_sms", methods=['GET', 'POST'])
def hello_monkey():
    """Respond and greet the caller by name."""
 
    body = request.values.get('Body', None)
    message = "You requested tides for %s" % body
 
    resp = twilio.twiml.Response()
    resp.message(message)
 
    return str(resp)

if __name__ == '__main__':
    app.run(debug=True)
