from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact

# Create your views here.
def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    
    user = auth.authenticate(username=username, password=password)
    if user is not None:
      auth.login(request, user)
      messages.success(request, 'You are now logged in.')
      return redirect('dashboard')
    else:
      messages.error(request, 'Invalid username or password.')
      return redirect('login')

  else:
    return render(request, 'accounts/login.html')

def register(request):
  if request.method == 'POST':
    # Get form values
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    # Check if password match
    if password == password2:
      
      # Check username
      if User.objects.filter(username=username).exists():
        messages.error(request, 'That username is taken.')
        return redirect('register')
      
      # Check email
      elif User.objects.filter(email=email).exists():
        messages.error(request, 'That email is already in use.')
        return redirect('register')
      
      # All good - register the user
      else:
        user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
        user.save()
        messages.success(request, 'You are now registered and can log in.')
        return redirect('login')

    else:
      messages.error(request, 'Passwords do not match.')
      return redirect('register')
  else:
    return render(request, 'accounts/register.html')

def logout(request):
  if request.method == 'POST':
    auth.logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('index')

def dashboard(request):
  user_contacts = Contact.objects.all().filter(user_id=request.user.id)

  context = {
    'contacts': user_contacts
  }

  return render(request, 'accounts/dashboard.html', context)