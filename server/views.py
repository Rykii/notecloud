from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def signIn(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None and user.is_active:
			login(request, user)
			print ('login successfully...')
			return HttpResponseRedirect('/home')
		else:
			error = json.dumps({errorCode: 10000, errorMessage: 'Invalid username or password!'})
			return JsonResponse(error)

