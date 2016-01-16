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
	are_you_human = forms.CharField(label='In Buddhism, which is the lowest of the Ten Worlds? (one word answer)', max_length=80)
	your_comment = forms.CharField(label='Your comments',
				widget=forms.Textarea)

def send_email(comment):
	recipients = ['siddharthmanu@gmail.com']	
	subject = '#WorldOfSoka New Comment from %s'%comment.commentor_email
	sender = 'noreply@worldofsoka.in' 
	try:
		send_mail(subject, comment.comment_text, sender, recipients)
	except:
		pass	

def add_form_feedback(form_data):
	if form_data['are_you_human'].strip().upper() !=  'HELL':
		return	
	c = Comment(commentor_name=form_data['your_name'],
			comment_text = form_data['your_comment'],
			commentor_email = form_data['your_email'])
	c.comment_date = timezone.now()
	send_email(c)
	c.save()
			
def get_feedback(request):
	#TODO: fix recaptcha. it always returns false
	context = songs.views.get_sidebar_context()

	if request.method == 'POST':
		post_data = request.POST
		meta_data = request.META
		form = FeedbackForm(post_data)

		if form.is_valid():
			add_form_feedback(form.cleaned_data)
			#clear the form if data is added. Else let the fields remain
			form = FeedbackForm()
		
	else:
		""" first time an empty form is displayed"""
		form = FeedbackForm()

	comments = Comment.objects.order_by('-comment_date')[:50]
	context['comments'] = comments 
	context['feedback_form'] = form
	return render(request, 'feedback/index.html', context)
