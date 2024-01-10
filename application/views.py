from django.shortcuts import render, HttpResponse
from datetime import datetime
from .forms import ContactForm
from .models import AllProjects  # Import your AllProjects model

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


# retrieves all the records from the AllProjects database table
all_projects = AllProjects.objects.all()




def about(request):
    return render(request, "mywebsite/about.html")

def academics(request):
    return render(request, "mywebsite/academics.html")





def llm(request):
    return render(request, "mywebsite/llm.html")

def upcoming(request):
    return render(request, "mywebsite/upcoming.html")



def contact_view(request):
    print("within contact view")
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'mywebsite/home.html')
    else:
        form = ContactForm()

    return render(request, 'mywebsite/contact.html', { 'form': form })



def allprojects(request):
    
    # Define a context dictionary to pass data to the template
    context = {
        'projects': all_projects,
    }
    
    # Render the template with the context data
    return render(request, 'mywebsite/allprojects.html', context)


def bitools(request):

    # Filter projects with project code starting with "DASH"
    projects = [project for project in all_projects if project.projectCode.lower().startswith("dash")]
    
    # Define a context dictionary to pass data to the template
    context = {
        'projects': projects,
    }
    return render(request, "mywebsite/bitools.html", context)



def sql(request):
    # Filter projects with project code starting with "DASH"
    projects = [project for project in all_projects if project.projectCode.lower().startswith("sql")]
    
    # Define a context dictionary to pass data to the template
    context = {
        'projects': projects,
    }
    return render(request, "mywebsite/sql.html", context)


def machinelearning(request):
    # Filter projects with project code starting with "DASH"
    projects = [project for project in all_projects if project.projectCode.lower().startswith("ml")]
    
    # Define a context dictionary to pass data to the template
    context = {
        'projects': projects,
    }
    return render(request, "mywebsite/machinelearning.html", context)


def streamlit(request):
    # Filter projects with project code starting with "DASH"
    projects = [project for project in all_projects if project.projectCode.lower().startswith("st")]
    
    # Define a context dictionary to pass data to the template
    context = {
        'projects': projects,
    }
    return render(request, "mywebsite/streamlit.html", context)


def django(request):
    # Filter projects with project code starting with "DASH"
    projects = [project for project in all_projects if project.projectCode.lower().startswith("django")]
    
    # Define a context dictionary to pass data to the template
    context = {
        'projects': projects,
    }
    return render(request, "mywebsite/django.html", context)



def eda(request):
    # Filter projects with project code starting with "DASH"
    projects = [project for project in all_projects if project.projectCode.lower().startswith("eda")]
    
    # Define a context dictionary to pass data to the template
    context = {
        'projects': projects,
    }
    return render(request, "mywebsite/eda.html", context)