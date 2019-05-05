from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
import json
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from .models import UserOptions

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

def signUp(request):
	if request.method == 'POST':
		reqJson = json.loads(request.body.decode())
		username = reqJson.get('username')
		password = reqJson.get('password')
		filter_result = User.objects.filter(username__exact=username)
		result = ''
		if len(filter_result) > 0:
			result = json.dumps({'errorCode': 10001, 'errorMessage': 'User already exists!'})
			# print('******************username='+username+', password='+password)
		else:
			user = User.objects.create_user(username=username, password=password, email='')
			user_options = UserOptions(user=user)
			user_options.save()
			result = json.dumps({'success': 1, 'message': 'Sign up successfully complete!'})
		return JsonResponse(result, safe = False)