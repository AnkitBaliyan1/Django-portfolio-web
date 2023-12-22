from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from .forms import ContactForm

# Create your views here.

def calculate_work_experience(start_date):
    # Calculate work experience
    current_date = datetime.now()
    start_date = datetime.strptime(start_date, '%Y-%m-%d')  # Convert the input date string to a datetime object
    delta = current_date - start_date
    years = delta.days // 365
    months = (delta.days % 365) // 30

    return f"{years} years and {months} months"

def home(request):
    start_date = "2021-09-20"  # Replace with your actual start date
    work_experience = calculate_work_experience(start_date)
    
    # Pass the work_experience variable to your template
    context = {'work_experience': work_experience}

    return render(request, 'mywebsite/home.html', context)

def about(request):
    return render(request, "mywebsite/about.html")

def academics(request):
    return render(request, "mywebsite/academics.html")

def machinelearning(request):
    return render(request, "mywebsite/machinelearning.html")

def sql(request):
    return render(request, "mywebsite/sql.html")

def bitools(request):
    return render(request, "mywebsite/bitools.html")

def llm(request):
    return render(request, "mywebsite/llm.html")

def upcoming(request):
    return render(request, "mywebsite/upcoming.html")

def contact(request):
    pass

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process and save the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            # Save the data to your data model or perform other actions
            # ...

            # Optionally, you can redirect the user to a success page
            # after processing the form data
            # return HttpResponseRedirect('/success/')

    else:
        form = ContactForm()

    return render(request, 'mywebsite/contact.html', {'form': form})