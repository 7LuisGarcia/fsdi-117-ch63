from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail


def about_me_view(request):
    return render(request, 'pages/about_me.html')
def experience_view(request):
    return render(request, 'pages/experience.html')
    
                  

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid(): 
            
            name = form.cleaned_data['name'] 
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = form.cleaned_data['subject']

            # Build the full email content
            message_body = (
                f'You have a new message from your Portfolio:\n\n'
                f'Name: {name}\n'
                f'Email: {email}\n'
                f'Message:\n{message}\n'
            )

            try:
                send_mail(
                    "Email From Portfolio",   # subject
                    message_body,             # message
                    email,                    # from email (user email)
                    ['garcia062785@gmail.com']  # your receiving email
                )

                # Clear the form after successful submission
                form = ContactForm()
                return render(request, 'pages/contact.html', {'form': form, 'success': True})

            except Exception as e:
                print(f'Error sending email: {e}')
                return render(request, 'pages/contact.html', {'form': form, 'error': True})

        else:
            print("Form is not valid")
            print(form.errors)
            return render(request, 'pages/contact.html', {'form': form})

    else:
        form = ContactForm()
        return render(request, 'pages/contact.html', {'form': form})
