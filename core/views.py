from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from core.models import PartiPolic, Mility, Voting
from django.urls import reverse
from django.db.models import Q
from django.contrib import messages
from . forms import MilitiForm




def index(request):
    politic = PartiPolic.objects.all()
    voting = Voting.objects.all()
    reach = request.POST.get('reach')
    if reach:
        politic = PartiPolic.objects.filter(Q(name__contains=reach)| 
                                            Q(user__contains=reach)|
                                            Q(choices_pati__contains=reach))
    else:
        voting = Voting.objects.all()
        
    return render(request, 'page/index.html', {'politic': politic, 'voting': voting})

def register(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        user = User.objects.create_user(username, email, password1 )
            
        if user.is_valid():
            user.save()
        return redirect('index')    
    else:
        messages.error(request, 'vous devais remplir tout champ')      
    return render(request, 'acounts/register.html')
"""
def mility(request, pk):
    vote = get_object_or_404(Voting, id=pk)
    user = request.user
    
    if user:
        vote.number_voting +=1
        vote.save()
        return redirect('index')
    elif vote.number_voting > 2:
        vote.number_voting.delete()
 
def detail_mility(request, pk):
    mility = get_object_or_404(Mility, id=pk)
    return render(request, 'page/vote.html', {'mility': mility})  
""" 

def formmility(request):
    
    if request.method == "POST":
        form = MilitiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MilitiForm()    
        
    return render(request, 'page/formmility.html', {'form': form})     