from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def user_view(request, user_id):
    # Retrieve the user information using the user_id
    # Replace the following lines with your actual implementation
    name = "Giorgi"
    surname = "Kvernadze"
    date_of_birth = "2004-01-12"
    years_passed = 18

    response = f"Name: {name}, Surname: {surname}, Date of Birth: {date_of_birth}, Years Passed: {years_passed}"
    return HttpResponse(response)
