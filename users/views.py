from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login

from django.contrib.auth import logout
from django.shortcuts import redirect

from django.contrib.auth.models import User

def user_login(request):
    if request.user.is_authenticated:
        current_user = request.user
        return render(request, 'user_account.html', {'current_user': current_user})
    else:
        current_user = None
        return render(request, 'user_login.html')
    
def validate_user(request):
    email = request.POST['email']
    password = request.POST['password']    
    # Authorize user
    user = authenticate(username=email, password=password)
    # User is NOT Authenticated
    if user is None:
        # Update result parameter to pass to view
        error_message = "Invalid Username or Password!"
        # Construct reverse URL for Http Response Redirect
        return render(request, 'user_login.html', {'error_message': error_message})
    else:
        # Login user 
        login(request, user)
        return HttpResponseRedirect(reverse('users:user_account'))
    
def user_account(request):
    print(request.user.username)
    if request.user.is_authenticated:
        return render(request, 'user_account.html', {   
            "firstname": request.user.first_name,
            "lastname": request.user.last_name,
            "email": request.user.username, })
    else:
        return HttpResponseRedirect(reverse('users:user_login'))

def user_add(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmpassword')

        # Create a New User & Save to Database
        try:
            if password == confirm_password:                
                user = User.objects.create_user(username=email, password=password)
                user.first_name = first_name
                user.last_name = last_name                                            
                user.is_staff = False
                user.is_superuser = False
                # Save user to Db
                user.save()
                # Redirect user
                return HttpResponseRedirect(reverse('users:user_account'))

        except Exception as ex:
                print(f'SOMETHING WENT WRONG!\nError:\n{str(ex)}')
                return render(request, 'user_add.html', {'error': str(ex)})
    else:
         return render(request, 'user_add.html')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:user_login'))

