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
@app.route("/", methods=["GET"])
def index():
	# query HackFood to get possible delivery
	output = ordrin_api.delivery_list("ASAP", "170 E 6th Street", "Claremont", "91711")
	text_body = createText(output)
	resp = twilio.twiml.Response()
	text = request.values.get("Body", None)
	resp.message(text)
	# message = client.messages.create(to="+15135605548", from_="+15132838068", body= text_body)
	return str(text)

if __name__ == '__main__':
    app.run(debug=True)
