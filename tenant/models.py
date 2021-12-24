from django.db import models

# Create your models here.

class Tenant(models.Model):
    name = models.CharField(max_length=100)
    subdomain = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.name) + ' - ' + '{}'.format(self.subdomain)

class TenentAwaredModel(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.tenant = Tenant.objects.get(pk=1)
        super().save(*args, **kwargs)

class Members(TenentAwaredModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.name)