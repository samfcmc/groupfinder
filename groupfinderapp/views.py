
import os
from django.shortcuts import render
import fenixedu

#Fenixedu client configuration
client_id = os.getenv('FENIXEDU_CLIENT_ID')
if(not client_id):
	# Use the file instead
	config = fenixedu.FenixEduConfiguration.fromConfigFile()
else:
	client_secret = os.getenv('FENIXEDU_CLIENT_SECRET')
	redirect_uri = os.getenv('FENIXEDU_REDIRECT_URI')
	base_url = os.getenv('FENIXEDU_BASE_URL')
	config = fenixedu.FenixEduConfiguration(client_id, redirect_uri, client_secret, base_url)

fenixEduClient = fenixedu.FenixEduClient(config)

# Create your views here.
def index(request):
	context = {'test': fenixEduClient.get_spaces()}
	return render(request, 'base.html', context)

