from django.db import models


class Member(models.Model):
    #Basic Fields
    first_name   = models.CharField(max_length=50, blank=False, null=False, verbose_name="First Name: ")
    last_name    = models.CharField(max_length=50, blank=False, null=False, verbose_name="Last Name: ")
    email        = models.CharField(max_length=50, blank=False, null=False, unique=True, verbose_name="Email: ")

    #Utility Fields
    created_at   = models.DateTimeField(auto_now_add=True, verbose_name="Created At: ", null=True)
    updated_at   = models.DateTimeField(auto_now=True, verbose_name="Updated At: ", null=True)
    slug         = models.SlugField(blank=True, unique=True, verbose_name="URL Snippet: ", help_text="Automatically Created. ")

    class Meta:
        verbose_name        = 'Member'
        verbose_name_plural = 'Members'
    
    #Object Representation
    def __str__(self):
        return f'Member - {self.first_name} {self.last_name} -'