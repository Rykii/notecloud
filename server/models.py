from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserOptions(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_first = models.BooleanField('是否首套')
    weight = models.CommaSeparatedIntegerField('权重', max_length=100)

class Area(models.Model):
    name = models.CharField('板块名称', max_length=100)

class Neighbor(models.Model):
    name = models.CharField('楼盘名称', max_length=100)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    address = models.CharField('地址', max_length=100)

class House(models.Model):
    neighbor = models.ForeignKey(Neighbor, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    square = models.DecimalField('面积', max_digits=10, decimal_places=2)
    rooms = models.CommaSeparatedIntegerField('房型', max_length=100)
    floor = models.CommaSeparatedIntegerField('楼层', max_length=10)
    age = models.IntegerField('年代')
    price = models.IntegerField('价格')
    tax_type = models.IntegerField('税费类型')
    lift_house = models.CommaSeparatedIntegerField('梯户比', max_length=10)
    image_path = models.URLField()

class AreaScore(models.Model):
    user = models.ForeignKey(UserOptions, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    area_score = models.IntegerField()

class NeighborScore(models.Model):
    user = models.ForeignKey(UserOptions, on_delete=models.CASCADE)
    neighbor = models.ForeignKey(Neighbor, on_delete=models.CASCADE)
    in_env_score = models.IntegerField()
    ex_env_score = models.IntegerField()
    trans_score = models.IntegerField()
    park_score = models.IntegerField()
    resource_score = models.IntegerField()

class HouseScore(models.Model):
    user = models.ForeignKey(UserOptions, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    neighbor = models.ForeignKey(Neighbor, on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    model_score = models.IntegerField()
    floor_score = models.IntegerField()
    age_score = models.IntegerField()
