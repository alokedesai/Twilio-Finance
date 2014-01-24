from flask import Flask, render_template, request, Response
import ordrin
from twilio.rest import TwilioRestClient
import twilio.twiml
import ystockquote
from twilio-info import *

app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.do')
app.jinja_env.add_extension('jinja2.ext.loopcontrols')
ordrin_api = ordrin.APIs("aDn9SOwqDwmdmAmi8Qcb-LGre8M5sY_-q15dXet9zVw")





client = TwilioRestClient(account_sid, auth_token)
def createText(result):
	output = ""
	for item in result:
		output += item["na"] + "-" + item["addr"]
		# new line for text
		output += "\n"
	return output
@app.route("/")
def index():
	# return str(ystockquote.get_last_trade_price("AAPL"))
	return "test"


@app.route("/sms", methods=["POST"])
def sms():
	# query HackFood to get possible delivery
	text = str(request.form["Body"].lower())

	if (text.startswith("change ")):
		text = text.replace("change" , "")

		output = ""
		companies = text.split(",")
		for company in companies:
			output += company.strip().upper() + ": " + ystockquote.get_change_percent_change(company.strip()) + "\n"
		resp = twilio.twiml.Response()
		resp.message(output)
	else:
		companies = text.split(",")
		output = ""
		for company in companies:
			output += company.strip().upper() + ": " + ystockquote.get_last_trade_price(company.strip()) + "\n"
		resp = twilio.twiml.Response()
		resp.message(output)
	# message = client.messages.create(to="+15135605548", from_="+15132838068", body= text_body)
	return str(resp)
 

if __name__ == '__main__':
    app.run(debug=True)
