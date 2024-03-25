from django.db import models

# Create your models here.
class StatusModel(models.Model):
  name = models.CharField(max_length=200)
  description = models.TextField()

  def __str__(self):
    return self.name
  
class JobTitle(models.Model):
  name = models.CharField(max_length=200)
  description = models.TextField()
  status = models.ForeignKey(StatusModel, 
                            related_name='status_status_model', 
                            blank = True, null = True, 
                            on_delete=models.SET_NULL)
  def __str__(self):
    return self.name