from django.shortcuts import render, redirect

# Methods.

def register(request):
  if request.method == "POST":
   #Register User
   return
  else:
    return render(request, 'accounts/register.html')

def dashboard(request):
  
 return render(request, 'accounts/dashboard.html')

def login(request):
  if request.method == "POST":
    # Login User
    return
  else :  
   return render(request, 'accounts/login.html')  

def logout(request):
  return redirect('index')    