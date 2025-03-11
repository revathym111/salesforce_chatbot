from django.shortcuts import render
from django.http import JsonResponse # returns a JSON response in a Django view, using the JsonResponse class from django.http
from .salesforce_api import get_customer_data

def chatbot_response(request):
    user_input = request.GET.get('message', '').lower()

    if "customer" in user_input:
        email = "rose@edge.com"
        customer = get_customer_data(email)
        if customer:
            return JsonResponse({"response": f"Customer Name: {customer['Name']}, Email: {customer['Email']}"})
        return JsonResponse({"response": "Customer not found in Salesforce"})
    return JsonResponse({"response": "I can help with customer details. Ask me something!"})

# Create your views here.
