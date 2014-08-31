
import os
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
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
	context = {'auth_url': fenixEduClient.get_authentication_url()}

	code = request.GET.get('code', None)
	if code is not None and not request.user.is_authenticated():
		user = authenticate(request=request, client=fenixEduClient, code=code)
		if user is not None:
			login(request, user)

	return render(request, 'base.html', context)

def user_logout(request):
	logout(request)
	context = {'auth_url': fenixEduClient.get_authentication_url()}
	return render(request, 'base.html', context)

