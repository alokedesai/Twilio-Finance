from flask import Flask, render_template, request, Response
import ordrin
from twilio.rest import TwilioRestClient
import twilio.twiml
import ystockquote
from twilioInfo import *

app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.do')
app.jinja_env.add_extension('jinja2.ext.loopcontrols')


client = TwilioRestClient(account_sid, auth_token)
def createText(method, companies):
	output = ""
	for company in companies:
		# properly format the output
		output += company.strip().upper() + ": " + method(company.strip()) + "\n"
	return output
@app.route("/")
def index():
	# return str(ystockquote.get_last_trade_price("AAPL"))
	return createText(ystockquote.get_last_trade_price, ["TWTR"])


@app.route("/sms", methods=["POST"])
def sms():
	# query HackFood to get possible delivery
	text = str(request.form["Body"].lower())

	if (text.startswith("price ")):
		text = text.replace("price", "")
		output = createText(ystockquote.get_last_trade_price, text.split(","))
		resp = twilio.twiml.Response()
		resp.message(output)
		return str(resp)
	elif (text.startswith("change ")):
		text = text.replace("change", "")
		output = createText(ystockquote.get_change_percent_change, text.split(","))
		resp = twilio.twiml.Response()
		resp.message(output)
		return str(resp)
	elif (text.startswith("pe ")):
		text = text.replace("pe", "")
		companies = text.split(",")
		output = createText(ystockquote.get_pe, companies)
		resp = twilio.twiml.Response()
		resp.message(output)
		return str(resp)
	elif (text.startswith("open ")):
		text = text.replace("open", "")
		companies = text.split(",")
		output = createText(ystockquote.get_today_open, companies)
		resp = twilio.twiml.Response()
		resp.message(output)
		return str(resp)
	elif (text.startswith("close ")):
		text = text.replace("close", "")
		companies = text.split(",")
		output = createText(ystockquote.get_previous_close, companies)
		resp = twilio.twiml.Response()
		resp.message(output)
		return str(resp)
	elif (text.startswith("low ")):
		text = text.replace("low", "")
		companies = text.split(",")
		output = createText(ystockquote.get_todays_low, companies)
		resp = twilio.twiml.Response()
		resp.message(output)
		return str(resp)
	elif (text.startswith("high ")):
		text = text.replace("high", "")
		companies = text.split(",")
		output = createText(ystockquote.get_todays_high, companies)
		resp = twilio.twiml.Response()
		resp.message(output)
		return str(resp)
	else:
		output = createText(ystockquote.get_last_trade_price, text.split(","))
		resp = twilio.twiml.Response()
		resp.message(output)
		return str(resp)
 

if __name__ == '__main__':
    app.run(debug=True)
