from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm, TextForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django import forms
from transformers import pipeline

model_path = "cardiffnlp/twitter-roberta-base-sentiment-latest"
sentiment_analyzer = pipeline("sentiment-analysis", model=model_path, tokenizer=model_path)

def analyze_sentiment(text):
    sentiment = sentiment_analyzer(text)
    return sentiment

#index
def index(request):

    sentiment = None
    if request.user.is_authenticated:
        
        if request.method == 'POST':
            
            Tform = TextForm(request.POST)
            if Tform.is_valid():
                user_input = Tform.cleaned_data['text']
                sentiment = analyze_sentiment(user_input)
        else:    
            Tform=TextForm()
            
        return render(request, 'user/index.html', {'form':Tform,'sentiment': sentiment,'title':'index'})

    else:
        return render(request, 'user/index.html', {'title':'index'})
  
#register here 
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form, 'title':'register here'})
  
#login forms
def Login(request):
    if request.method == 'POST':
  
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' welcome {username} !!')
            return redirect('index')
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'user/login.html', {'form':form, 'title':'log in'})

