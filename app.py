from flask import Flask, render_template, request, Response
import ordrin
from twilio.rest import TwilioRestClient
import twilio.twiml

app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.do')
app.jinja_env.add_extension('jinja2.ext.loopcontrols')
ordrin_api = ordrin.APIs("aDn9SOwqDwmdmAmi8Qcb-LGre8M5sY_-q15dXet9zVw")


# Twilio Information
account_sid = "AC48821ab395054c9d8a5f4bc69ec165f8"
auth_token = "bfc8dcab5be8bbf054c8c8e8c19aadc9"
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
	return "index"
@app.route("/sms", methods=["POST"])
def sms():
	# query HackFood to get possible delivery
	text = request.form["Body"]

	#split on commas
	address = text.split(",")
	output = ordrin_api.delivery_list("ASAP", address[0], address[1], address[2])
	# text_body = createText(output)
	resp = twilio.twiml.Response()
	
	resp.message(createText(output))
	# message = client.messages.create(to="+15135605548", from_="+15132838068", body= text_body)
	return str(resp)

if __name__ == '__main__':
    app.run(debug=True)
