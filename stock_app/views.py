from django.shortcuts import render
import finnhub

# Create your views here.
def home(request):
    finnhub_client = finnhub.Client(api_key="bt1fg7f48v6qjjkjlvvg")
    res = finnhub_client.stock_candles('AAPL', 'D', 1590988249, 1591852249)
    res1 = finnhub_client.company_profile2(symbol='AAPL')
    new = finnhub_client.company_news('AAPL', _from="2020-06-01", to="2020-06-10")
    financial = finnhub_client.company_basic_financials('AAPL', 'margin')
    return render(request, 'home.html', {'response': res, 'response1': res1, 'response_new': new, 'financial': financial})
