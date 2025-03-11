#  Salesforce-Integrated Chatbot using Django & Python (Customer Support Automation System)

A **Django-based chatbot** that integrates with **Salesforce API** to fetch customer details based on user input. It dynamically requests an email for customer lookup and returns real-time responses.

---

##  Features  
- 1. **Django & Python** backend for chatbot processing.  
- 2. **Salesforce API Integration** to retrieve customer details.  
- 3. **RESTful API** that accepts user input and fetches customer data dynamically.  
- 4. **JSON Response Output** for seamless API consumption.  
- 5. **Virtual Environment Setup** for smooth dependency management.  
- 6. **Deployment Ready** for **Render**.  

---

##  Project Structure  
salesforce_chatbot/ 
    │── salesforce_chatbot_app/ # Main Django chatbot app 
       │──chatbot/ 
            | |── apps.py
            │ ├── views.py # Chatbot logic (Handles API requests) 
            | │── salesforce_api.py/ # Salesforce Integration 
        │──salesforce_chatbot
            │ ├── urls.py # API routes 
            │ ├── settings.py
        │── manage.py # Django management commands
        │── requirements.txt  
    │── README.md # Project Documentation 
    │── .env # Environment Variables (Ignored in Git) 
    │── .gitignore # Ignore unnecessary files
        
# Successfully started the Django server in a activated virtual environment
    The server will start at http://127.0.0.1:8000/
    python manage.py runserver

# Tested the API functionality using Insomnia.

## Unique advantages over Salesforce’s inbuilt Einstein bots?

--> Cost-effective especially for businesses with budget constraints(Expensive Salesforce licenses)

--> Can be fully customized to fit business needs, integrate with external systems, and use custom AI models. Can integrate with OpenAI (GPT), Google Dialog Flow, or custom NLP models for better responses. Can be integrated into Slack, WhatsApp, Websites, Mobile Apps, and Emails while still syncing with Salesforce.(Einstein Bots limited to Salesforce Configurations and UI)

--> Can log interactions into Salesforce and external databases (PostgreSQL, MongoDB, etc.)(Stores data mainly inside Salesforce)

