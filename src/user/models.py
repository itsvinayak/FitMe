from django.db import models
from django.contrib.auth.models import User
from datetime import datetime





class Trainer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    trainer = models.BooleanField('trainer', default=True)
    approve = models.BooleanField(default=False)

    def __str__(self):
       return self.user.username

    class Meta:
        db_table = "trainer"




class Trainee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    trainee = models.BooleanField('trainee', default=True)
    trainer_ass = models.OneToOneField(Trainer,null=True,on_delete=models.SET_NULL)
    count_code = models.CharField(max_length=3)
    phone = models.CharField(max_length=11,unique=True)
    dob = models.DateField(default=datetime.now)
    gender = models.CharField(max_length=6,default='Male')

    def __str__(self):
       return f"{self.user.username} profile details"

    class Meta:
        db_table = "trainee"



class TraineeAddress(models.Model):
    house_no = models.IntegerField()
    street_no = models.IntegerField()
    village = models.CharField(max_length=30)
    post = models.CharField(max_length=30)
    dist_city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    pincode = models.IntegerField()

    def __str__(self):
       return f"{self.user.username} 's address"

    class Meta:
        db_table = "trainee_address"



class TraineePhy(models.Model):
    height = models.DecimalField(max_digits=3, decimal_places=2)
    age = models.IntegerField()
    current_weight = models.DecimalField(max_digits=3, decimal_places=2)
    goal_weight = models.DecimalField(max_digits=3, decimal_places=2)
    health_condition = models.CharField(max_length=50)

    def __str__(self):
       return f"{self.user.username} trainee phyk"

    class Meta:
        db_table = "trainee_phy"
