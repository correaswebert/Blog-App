from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


def register(request):
    """create a registration form using built-in one"""

    # process the form only if it is of POST type
    # otherwise just redirect to the same page
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # creates new user
            form.save()

            # cleaning parses the form data into python dictionary
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account has been created! Login now.')

            # on success, instead of redirecting to the same page (default)
            # redirect to the login page
            return redirect('login')
    else:
        form = UserRegisterForm()

    # in case of invalid form, redirect to same page, keeping the fields
    # intact (except password fields) and passing error messages
    return render(request, 'users/register.html', {'form': form})


# don't allow access to this page (by manually typing url)
# if the user is not authenticated -> login_required
@login_required
def profile(request):
    """allow users to update their profile"""
    return render(request, 'users/profile.html')
