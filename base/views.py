from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import Parameter
from scipy.stats import poisson
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(request):
    if request.method == 'POST':
        parameter = Parameter.objects.create(
            
            home_name = request.POST.get('home_name'),
            home_goals = request.POST.get('home_scored'),
            home_conceded = request.POST.get('home_conceded'),
            home_league_avg = request.POST.get('home_league_avg'),
            away_name = request.POST.get('away_name'),
            away_goals = request.POST.get('away_scored'),
            away_conceded = request.POST.get('away_conceded'),
            away_league_avg = request.POST.get('away_league_avg'),
            home_results = float(request.POST.get('home_scored'))/float(request.POST.get('home_league_avg')) * float(request.POST.get('away_conceded'))/float(request.POST.get('home_league_avg')) * float(request.POST.get('home_league_avg')),
            away_results = float(request.POST.get('away_scored'))/float(request.POST.get('away_league_avg')) * float(request.POST.get('home_conceded'))/float(request.POST.get('away_league_avg')) * float(request.POST.get('away_league_avg')),
            over_three = (1-poisson.cdf(k=3, mu=float(request.POST.get('home_scored'))/float(request.POST.get('home_league_avg')) * float(request.POST.get('away_conceded'))/float(request.POST.get('home_league_avg')) * float(request.POST.get('home_league_avg'))+
                float(request.POST.get('away_scored'))/float(request.POST.get('away_league_avg')) * float(request.POST.get('home_conceded'))/float(request.POST.get('away_league_avg')) * float(request.POST.get('away_league_avg'))))*100,
            over_two = (1-poisson.cdf(k=2, mu=float(request.POST.get('home_scored'))/float(request.POST.get('home_league_avg')) * float(request.POST.get('away_conceded'))/float(request.POST.get('home_league_avg')) * float(request.POST.get('home_league_avg'))+
                float(request.POST.get('away_scored'))/float(request.POST.get('away_league_avg')) * float(request.POST.get('home_conceded'))/float(request.POST.get('away_league_avg')) * float(request.POST.get('away_league_avg'))))*100,
            home_resulsint = ("{:0.2f}".format(float(request.POST.get('home_scored'))/float(request.POST.get('home_league_avg')) * float(request.POST.get('away_conceded'))/float(request.POST.get('home_league_avg')) * float(request.POST.get('home_league_avg')))),
            away_resultsint = ("{:0.2f}".format(float(request.POST.get('away_scored'))/float(request.POST.get('away_league_avg')) * float(request.POST.get('home_conceded'))/float(request.POST.get('away_league_avg')) * float(request.POST.get('away_league_avg')))),
            overthreeint = ("{:0.2f}".format((1-poisson.cdf(k=3, mu=float(request.POST.get('home_scored'))/float(request.POST.get('home_league_avg')) * float(request.POST.get('away_conceded'))/float(request.POST.get('home_league_avg')) * float(request.POST.get('home_league_avg'))+
                float(request.POST.get('away_scored'))/float(request.POST.get('away_league_avg')) * float(request.POST.get('home_conceded'))/float(request.POST.get('away_league_avg')) * float(request.POST.get('away_league_avg'))))*100)),
            overtwoint = ("{:0.2f}".format((1-poisson.cdf(k=2, mu=float(request.POST.get('home_scored'))/float(request.POST.get('home_league_avg')) * float(request.POST.get('away_conceded'))/float(request.POST.get('home_league_avg')) * float(request.POST.get('home_league_avg'))+
                float(request.POST.get('away_scored'))/float(request.POST.get('away_league_avg')) * float(request.POST.get('home_conceded'))/float(request.POST.get('away_league_avg')) * float(request.POST.get('away_league_avg'))))*100)),
        )
        
        parameter.save()
        return redirect(home)

    


    return render(request, 'index.html')

def result(request):
    
    results = Parameter.objects.all()

    context = { 'results':results}
    return render(request, 'result.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'signin.html')

    return render(request, 'signin.html')


def logoutUser(request):
    logout(request)
    return redirect('home')