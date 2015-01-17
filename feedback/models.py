from django.db import models

class Comment(models.Model):
	commentor_name = models.CharField(max_length=100)
	comment_date = models.DateTimeField('comment date')
	commentor_email = models.CharField(max_length=100)
	comment_text = models.CharField(max_length=5000)
	
	def __unicode__(self):
		return "By %s on %s"%(self.commentor_name,
				str(self.comment_date))	
