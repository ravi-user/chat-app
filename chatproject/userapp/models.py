from django.db import models
# Create your models here.


class User(models.Model):
    username = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=20)
    profile_pic = models.FileField(upload_to="media/images")
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True,blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)


    def __str__(self):
        return self.username

class Detail(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    value = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True,blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)

    def __str__(self):
        return self.sender.username+" "+self.receiver.username +" "+self.value

class Group(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.TextField(max_length=500)
    people = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True,blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)

    def __str__(self):
        return self.sender_id.username

        