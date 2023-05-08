from django.db import models

class Topic(models.Model):
    """The topic that the user is learning."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns the string representation of the model."""
        return self.text
