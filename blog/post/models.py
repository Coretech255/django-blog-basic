from django.db import models

# Article Model
class Article(models.Model):

	title = models.CharField(max_length=200)
	preview = models.TextField(max_length=500)
	content = models.TextField(max_length=1000)
	posted = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title