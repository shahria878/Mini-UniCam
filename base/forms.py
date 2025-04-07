from django import forms
from .models import CourseRegistration, Course

class CourseRegistrationForm(forms.ModelForm):
    courses = forms.ModelMultipleChoiceField(
        queryset=Course.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = CourseRegistration
        fields = ['student_name', 'student_id', 'courses']
