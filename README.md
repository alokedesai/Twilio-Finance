# Twilio-Finance

**Twilio Finance** is a simple Twilio app that texts you stock quotes. 

To access simply text 513 283-8068 with the ticker of the company whose stock price you want. To access the price of Facebook, for example, simply text: `FB`. 

You can also get the prices of many companies at once by texting comma-delimited tickers: `FB, TWTR, GOOG`

To access the nominal and percent change of a company during the current business day, just add `change` to the text message: `change AAPL`.


##Example Usage
    Text:
    high FB,TWTR,GOOG 
    Response:
    FB: 56.26
    TWTR: 62.62
    GOOG: 1153.545"
    
    Text:
    AAPL
    Response:
    AAPL: 546.07
    
    Text:
    change TWTR, AAPL
    Reponse:
    TWTR: "-1.06 - -1.69%"
    AAPLE: "-10.11" - -1.82%"
   
##Suported Methods
* Current Price: no method
* Change (% & $): `change`
* P/E: `pe`
* Open Price: `open`
* Close Price: `close`
* High Price: `high`
* Low Price: `low`
