from flask import Flask, render_template, request, Response
import ordrin
from twilio.rest import TwilioRestClient
import twilio.twiml
import ystockquote
from twilioInfo import *

app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.do')
app.jinja_env.add_extension('jinja2.ext.loopcontrols')
ordrin_api = ordrin.APIs("aDn9SOwqDwmdmAmi8Qcb-LGre8M5sY_-q15dXet9zVw")





client = TwilioRestClient(account_sid, auth_token)
def createText(method, companies):
	output = ""
	for company in companies:
		output += company.strip() + ": " + method(company.strip()) + "\n"
	return output
@app.route("/")
def index():
	# return str(ystockquote.get_last_trade_price("AAPL"))
	return createText(ystockquote.get_last_trade_price, ["TWTR"])


@app.route("/sms", methods=["POST"])
def sms():
	# query HackFood to get possible delivery
	text = str(request.form["Body"].lower())
	
	if (text.startswith("change ")):
		text = text.replace("change","")
		companies = text.split(",")
		output = createText(ystockquote.get_change_percent_change, companies)
		resp = twilio.twiml.Response()
		resp.message(output)
	elif (text.startswith("pe ")):
		text = text.replace("pe","")
		companies = text.split(",")
		output = createText(ystockquote.get_pe, companies)
		resp = twilio.twiml.Response()
		resp.message(output)
	else:
		output = createText(ystockquote.get_last_trade_price, companies)
		resp = twilio.twiml.Response()
		resp.message(output)
	# message = client.messages.create(to="+15135605548", from_="+15132838068", body= text_body)
	return str(resp)
 

if __name__ == '__main__':
    app.run(debug=True)
