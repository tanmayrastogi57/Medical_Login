
from .forms import CustomUserCreationForm, PatientProfileForm, DoctorProfileForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm  # Import AuthenticationForm


def user_type_selection(request):
    # This view displays buttons to select either 'Patient' or 'Doctor'
    return render(request, 'users/user_type_selection.html')

def redirect_to_signup(request, user_type):
    # Redirects the user to the respective signup form
    if user_type == 'patient':
        return redirect('patient_signup')
    elif user_type == 'doctor':
        return redirect('doctor_signup')
    return redirect('user_type_selection')  # If something goes wrong, go back to selection


def signup_view(request):
    # Check the user type from the URL
    user_type = request.resolver_match.url_name

    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)

        # Initialize appropriate forms based on user type
        if user_type == 'patient_signup':
            profile_form = PatientProfileForm(request.POST, request.FILES)
        else:
            profile_form = DoctorProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            if user_type == 'patient_signup':
                user.is_patient = True
            else:
                user.is_doctor = True
            user.save()

            # Save profile form based on user type
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            login(request, user)
            if user_type == 'patient_signup':
                return redirect('patient_dashboard')
            elif user_type == 'doctor_signup':
                return redirect('doctor_dashboard')


    else:
        user_form = CustomUserCreationForm()
        if user_type == 'patient_signup':
            profile_form = PatientProfileForm()
        else:
            profile_form = DoctorProfileForm()

    return render(request, 'users/signup.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'user_type': user_type,
    })


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to appropriate dashboard
                if hasattr(user, 'patientprofile'):
                    return redirect('patient_dashboard')
                elif hasattr(user, 'doctorprofile'):
                    return redirect('doctor_dashboard')
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = AuthenticationForm()

    return render(request, 'users/login.html', {'form': form})


def patient_dashboard(request):
    # Display patient's dashboard with their details
    return render(request, 'users/patient_dashboard.html', {'user': request.user})

def doctor_dashboard(request):
    # Display doctor's dashboard with their details
    return render(request, 'users/doctor_dashboard.html', {'user': request.user})
