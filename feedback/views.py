from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.utils import timezone

from django.core.mail import send_mail

from songs.models import Song
from feedback.models import Comment 
import songs


class FeedbackForm(forms.Form):
	your_name = forms.CharField(label='Your name', max_length=50)
	your_email = forms.EmailField(label='Your email', max_length=50)
	your_comment = forms.CharField(label='Your comments',
				widget=forms.Textarea)

def send_email(comment):
	recipients = ['siddharthmanu@gmail.com']	
	subject = '#WorldOfSoka New Comment' 
	sender = comment.commentor_email
	try:
		send_mail(subject, comment.comment_text, sender, recipients)
	except:
		pass	

def add_form_feedback(form_data):
	c = Comment(commentor_name=form_data['your_name'],
			comment_text = form_data['your_comment'],
			commentor_email = form_data['your_email'],
			comment_date = timezone.now())
	send_email(c)
	c.save()
			
def get_feedback(request):
	context = songs.views.get_sidebar_context()

	if request.method == 'POST':
		form = FeedbackForm(request.POST)

		if form.is_valid():
			add_form_feedback(form.cleaned_data)	
			return HttpResponseRedirect('/feedback/')

	else:
		""" first time an empty form is displayed"""
		form = FeedbackForm()

	comments = Comment.objects.all()
	context['feedback_form'] = form
	context['comments'] = comments 
	return render(request, 'feedback/index.html', context)
