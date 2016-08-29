from django.db import models


class ContactModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    sended = models.BooleanField(default=False)
    date_of_send = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name