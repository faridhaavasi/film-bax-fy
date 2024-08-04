from django.db import models
from film_box.common.models import Basemodel
from django.contrib.auth import get_user_model

User = get_user_model()

class Logger(Basemodel):
    url = models.URLField(max_length=512)
    request = models.JSONField(null=True, blank=True)
    response = models.JSONField(null=True, blank=True)
    method = models.CharField(max_length=32)
    status = models.PositiveIntegerField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='logger', null=True, blank=True)
    
