from django.shortcuts import render, redirect
from .models import Student
from .models import Result
from .forms import CourseRegistrationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
 return render(request, "home.html", {})

def admit_view(request):
    return render(request, 'admit.html')

def result_view(request):
    results = Result.objects.all()
    return render(request, 'result.html', {'results': results})


def authView(request):
 if request.method == "POST":
  form = UserCreationForm(request.POST or None)
  if form.is_valid():
   form.save()
   return redirect("base:login")
 else:
  form = UserCreationForm()
 return render(request, "registration/signup.html", {"form": form})


def evolution_view(request):
    # You can fetch real data from a model later
    dummy_data = [
        {'name': 'John Doe', 'course': 'Math', 'progress': 80},
        {'name': 'Jane Smith', 'course': 'Science', 'progress': 92},
        {'name': 'Mike Johnson', 'course': 'History', 'progress': 76},
    ]
    return render(request, 'evolution.html', {'data': dummy_data})


def student_info_view(request):
    students = Student.objects.all()
    return render(request, 'student_info.html', {'students': students})



def course_registration_view(request):
    if request.method == 'POST':
        form = CourseRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_success')
    else:
        form = CourseRegistrationForm()
    return render(request, 'course_registration.html', {'form': form})

def registration_success(request):
    return render(request, 'registration_success.html')


