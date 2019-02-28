from django.contrib.auth.models import User
...

class Entry(models.Model):

    user = models.ForeignKey(User)      # The default django auth model has been extended.
    title = models.CharField(max_length=200)
