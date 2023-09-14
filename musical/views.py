from django.shortcuts import render

#home function
def home(request):
    if request.user.is_authenticated:
        current_user = request.user
        return render(request, 'home.html', {'current_user': current_user})
    else:
        return render(request, 'home.html')
    
#intro function
def intro(request):
    if request.user.is_authenticated:
        current_user = request.user
        return render(request, 'intro.html', {'current_user': current_user})
    else:
        return render(request, 'intro.html')
    
#about function
def about(request):
    if request.user.is_authenticated:
        current_user = request.user
        return render(request, 'about.html', {'current_user': current_user})
    else:
        return render(request, 'about.html')