from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


monthly_challenges = {
    "january": "Eat no meat for entire month!",
    "february": "Walk for at least 20 minutes every day",
    "march": "Learn Django for at least 30 minutes",
    "april": "Read books for 30 days in this month",
    "may": "Watch a new tv series",
    "june": "Go for hiking this month",
    "july": "Visit temple each day",
    "august": "Exercise HIIT workout in this month",
    "september": "Learn Python OOP concept for at least 30 minutes",
    "october": "Learn driving",
    "november": "Watch cricket world cup this month",
    "december": "Learn swimming for 1 hour daily",
}

# Create your views here.

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        captialized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items+= f"<li><a href=\"{month_path}\">{captialized_month}</a></li>"

    #<li><a href=".."></li>.....<li><a href = ".."></li>
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challenge_number(resuest, month):
    months = list(monthly_challenges.keys())

    if month>len(months):
        return HttpResponseNotFound("Invalid month")
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) # challenges/january
                                                                      # use reverse function instead of manually encoding path
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
    

    


