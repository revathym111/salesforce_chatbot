from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch
from chatbot.salesforce_api import get_customer_data

class ChatbotAPITestCase(TestCase):
    def setUp(self):
        #Setup a test client for API requests
        self.client = Client()
        self.chatbot_url = reverse('chatbot_response')

    @patch('salesforce_api.get_customer_data')
    def test_chatbot_customer_found(self, mock_get_customer_data):
        #Test API response when customer is found
        mock_get_customer_data.return_value = {'Name': 'Rose Edge', 'Email': 'rose@edge.com'}
        response = self.client.get(self.chatbot_url, {'message': 'customer', 'email': 'unknown@edge.com'})
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.conten, {"response": "Customer not found in Salesforce"})

    @patch('salesforce_api.get_customer_data')
    def test_chatbot_no_email_provided(self):
        response = self.client.get(self.chatbot_url, {'message': 'customer'})
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {"response": "Please provide the customer's email address to proceed."})

    def test_chatbot_invalid_message(self):
        response = self.client.get(self.chatbot_url, {'message': 'hello'})
        self.assertEqual(response.sttaus_code, 200)
        self.assertJSONEqual(response.content, {"response": "I can help with customer details. Ask me something!"})
