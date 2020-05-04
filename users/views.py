from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    # process the form only if it is of POST type
    # otherwise just redirect to the same page
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # creates new user
            form.save()

            # cleaning parses the form data into python dictionary
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')

            # on success, instead of redirecting to the same page (default)
            # redirect to the homepage
            return redirect('blog-home')
    else:
        form = UserRegisterForm()

    # in case of invalid form, redirect to same page, keeping the fields
    # intact (except password fields) and passing error messages
    return render(request, 'users/register.html', {'form': form})
