from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
import json
from django.http import JsonResponse, HttpResponseRedirect

def signIn(request):
	if request.method == 'POST':
		reqJson = json.loads(request.body.decode())
		username = reqJson.get('username')
		password = reqJson.get('password')
		# print('******************username='+username+', password='+password)
		user = authenticate(username=username, password=password)
		# print('******************user is not None: '+str(user is not None))
		# print('******************user.is_active: '+str(user.is_active))
		if user is not None and user.is_active:
			login(request, user)
			print ('login successfully...')
			return HttpResponseRedirect('/home')
		else:
			error = json.dumps({'errorCode': 10000, 'errorMessage': 'Invalid username or password!'})
			return JsonResponse(error, safe = False)

def home():
	pass