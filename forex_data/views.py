from django.shortcuts import render
from oandapyV20 import API
import oandapyV20.endpoints.pricing as pricing
from .models import Price
from django.http import JsonResponse
from statistics import mean
import json
import datetime
import pytz
##oanda api key and request parameters
tz = pytz.timezone('Africa/Johannesburg')
oanda_count_id = "101-004-13311328-001" 
oanda_api = API(access_token="d2ec88eebf079e6d69bc4df508702b23-e33199e10ee5059e422d1951ca70a75f")
params ={"instruments": "EUR_USD"}
def index(request):
    ##make a request to get the latest price of EUR to USD and save to database
    stored_prices = latest_prices("non-json")
    ##render UI
    template_url = "forex_data/index.html"
    return render(request, template_url, stored_prices)



def chart_data(request):
    if request.GET["type"] == "get_chart_data":
        latest_price_data = Price.objects.all().order_by("-date")[:10]
        prices = []
        dates = []
        for item in latest_price_data:
            prices.append(item.price)
            dates.append(item.date.strftime('%Y-%m-%d %H:%M:%S'))
        return JsonResponse({"dates":dates, "prices":prices})
    else:
      price_data = latest_prices("json")
      return price_data

def latest_prices(type):
    ##make a request to get the latest price of EUR to USD and save to database
    api_pricing = pricing.PricingInfo(accountID=oanda_count_id, params=params)
    api_pricing_request = oanda_api.request(api_pricing)
    new_price_record = Price()
    new_price_record.price = api_pricing.response["prices"][0]["bids"][0]["price"]
    new_price_record.save()
    ##get the maximum
    ##minimum and averge price of the last 100 prices
    latest_prices = Price.objects.all().order_by("-date")[:100]
    prices = []
    prices_and_dates = []
    max_price = 0
    min_price = 0
    avg_price =0
    for count, price in enumerate(latest_prices):
        prices.append(price.price)
        shaded = False
        if count%2 == 0:
            shaded = True
        prices_and_dates.append({"date":price.date,"price":price.price,"count":count,"shaded":shaded})
    max_price = max(prices)
    min_price = min(prices)
    avg_price = mean(prices)
    # return the minimum, mximum and average of last 100 prices and the last 100 prices
    # average is rounded off to 4 decimal places
    if type == "non-json":
        response = {"min":min_price, "max":max_price,"avg":round(avg_price,4),"table_data":prices_and_dates}
    else:
        response = JsonResponse({"min":min_price, "max":max_price,"avg":round(avg_price,4),"table_data":prices_and_dates})
    return response 



