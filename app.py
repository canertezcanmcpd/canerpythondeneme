# -*- coding:utf8 -*-
# !/usr/bin/env python
# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import print_function
from future.standard_library import install_aliases
install_aliases()

from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError

import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = processRequest(req)

    res = json.dumps(res, indent=4)
    # print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


def processRequest(req):
    condition = req.get("result").get("action")
    if condition == "test":
        return {"speech": "claim","displayText": "claim","source": "apiai-weather-webhook-sample"}
    elif condition == "claimsStatus":
        return claims(req)
    elif condition == "sales":
        return sales(req)
    elif condition == "nps":
        return nps(req)
    elif condition == "game":
        return game(req)
    elif condition == "fundrecommendation":
        return fundrecommendation(req)		
    elif condition == "getinvestmentDetail":
        return getinvestmentDetail(req)		
    elif condition == "getfunddetail":
        return getfunddetail(req)	
    elif condition == "getnamesurname":
        return getnamesurname(req)			
    elif condition == "isusersbirthday":
        return isusersbirthday(req)			
    else:
    	baseurl = "https://query.yahooapis.com/v1/public/yql?"
    	yql_query = makeYqlQuery(req)
    	if yql_query is None:
            return {}
    	yql_url = baseurl + urlencode({'q': yql_query}) + "&format=json"
    	result = urlopen(yql_url).read()
    	data = json.loads(result)
    	res = makeWebhookResult(data)
    	return res

def isusersbirthday(req):
    baseurl = 'http://asknnapi.azurewebsites.net/api/contact/IsUsersBirthday?'	
    result = req.get("result")   
    parameters = result.get("parameters")
    polid = parameters.get("polid")
    yql_url = baseurl + urlencode({'polid': polid}) + "&format=json"
    resp = urlopen(yql_url).read()
    data = json.loads(resp)
    return {"speech": data,"displayText": data,"source": "apiai-weather-webhook-sample"}		
		
def getnamesurname(req):
    baseurl = 'http://asknnapi.azurewebsites.net/api/contact/GetNameSurname?'	
    result = req.get("result")   
    parameters = result.get("parameters")
    polid = parameters.get("polid")
    yql_url = baseurl + urlencode({'polid': polid}) + "&format=json"
    resp = urlopen(yql_url).read()
    data = json.loads(resp)
    return {"speech": data,"displayText": data,"source": "apiai-weather-webhook-sample"}			
		
def getfunddetail(req):
    baseurl = 'http://asknnapi.azurewebsites.net/api/contact/GetFundDetail?'	
    result = req.get("result")   
    parameters = result.get("parameters")
    polid = parameters.get("polid")
    yql_url = baseurl + urlencode({'polid': polid}) + "&format=json"
    resp = urlopen(yql_url).read()
    data = json.loads(resp)
    return {"speech": data,"displayText": data,"source": "apiai-weather-webhook-sample"}	

		
def getinvestmentDetail(req):
    baseurl = 'http://asknnapi.azurewebsites.net/api/contact/GetInvestmentDetail?'	
    result = req.get("result")   
    parameters = result.get("parameters")
    polid = parameters.get("polid")
    yql_url = baseurl + urlencode({'polid': polid}) + "&format=json"
    resp = urlopen(yql_url).read()
    data = json.loads(resp)
    return {"speech": data,"displayText": data,"source": "apiai-weather-webhook-sample"}		

def claims(req):
    baseurl = 'http://asknnapi.azurewebsites.net/api/contact/ClaimsStatus?'	
    result = req.get("result")   
    parameters = result.get("parameters")
    identityNumber = parameters.get("identityNumber")
    yql_url = baseurl + urlencode({'identityNumber': identityNumber}) + "&format=json"
    resp = urlopen(yql_url).read()
    data = json.loads(resp)
    return {"speech": data,"displayText": data,"source": "apiai-weather-webhook-sample"}
	
def fundrecommendation(req):
    baseurl = 'http://asknnapi.azurewebsites.net/api/contact/FundRecommendation?'	
    result = req.get("result")   
    parameters = result.get("parameters")
    identityNumber = parameters.get("identityNumber")
    polid = parameters.get("polid")
    yql_url = baseurl + urlencode({'identityNumber': identityNumber,'polid':polid}) + "&format=json"
    resp = urlopen(yql_url).read()
    data = json.loads(resp)
    return {"speech": data,"displayText": data,"source": "apiai-weather-webhook-sample"}	
	
def sales(req):
    baseurl = 'http://asknnapi.azurewebsites.net/api/contact/Sales?'	
    result = req.get("result")   
    parameters = result.get("parameters")
    nameSurname = parameters.get("nameSurname")
    phone = parameters.get("phone")
    product = parameters.get("product")	
    yql_url = baseurl + urlencode({'nameSurname': nameSurname,'phone':phone,'product':product}) + "&format=json"
    resp = urlopen(yql_url).read()
    data = json.loads(resp)
    return {"speech": data,"displayText": data,"source": "apiai-weather-webhook-sample"}		

def nps(req):
    baseurl = 'http://asknnapi.azurewebsites.net/api/contact/Nps?'	
    result = req.get("result")   
    parameters = result.get("parameters")
    answer = parameters.get("answer")    
    yql_url = baseurl + urlencode({'answer': answer}) + "&format=json"
    resp = urlopen(yql_url).read()
    data = json.loads(resp)
    return {"speech": data,"displayText": data,"source": "apiai-weather-webhook-sample"}
	
def game(req):
    baseurl = 'http://asknnapi.azurewebsites.net/api/contact/Game?'	
    result = req.get("result")   
    parameters = result.get("parameters")
    nickName = parameters.get("nickName")
    ans1 = parameters.get("ans1")
    ans2 = parameters.get("ans2")
    ans3 = parameters.get("ans3")
    yql_url = baseurl + urlencode({'nickName': nickName,'ans1':ans1,'ans2':ans2,'ans3':ans3}) + "&format=json"
    resp = urlopen(yql_url).read()
    data = json.loads(resp)
    return {"speech": data,"displayText": data,"source": "apiai-weather-webhook-sample"}

def makeYqlQuery(req):
    result = req.get("result")
    parameters = result.get("parameters")
    city = parameters.get("geo-city")
    if city is None:
        return None

    return "select * from weather.forecast where woeid in (select woeid from geo.places(1) where text='" + city + "')"


def makeWebhookResult(data):
    query = data.get('query')
    if query is None:
        return {}

    result = query.get('results')
    if result is None:
        return {}

    channel = result.get('channel')
    if channel is None:
        return {}

    item = channel.get('item')
    location = channel.get('location')
    units = channel.get('units')
    if (location is None) or (item is None) or (units is None):
        return {}

    condition = item.get('condition')
    if condition is None:
        return {}

    # print(json.dumps(item, indent=4))
    
    speech = "Today " + location.get('city') + ": " + condition.get('text') +" "+ condition.get('temp')+ units.get('temperature') 
	
    if "Clear" in condition.get('text'):
        speech += " You can take the sunglasses <span class='glyphicon glyphicon-sunglasses'></span>"
    elif "Rain" in condition.get('text'):
        speech +=" You must take the umbrella"
    elif "Cloudy" in condition.get('text'):
        speech += " You can take the umbrella"
    elif "Sunny" in condition.get('text'):
        speech += " You must take the sunglasses <span class='glyphicon glyphicon-sunglasses'></span>"

	

    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        # "data": data,
        # "contextOut": [],
        "source": "apiai-weather-webhook-sample"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')
