from django.db import models
from django.contrib.auth.models import User
from django.core.validators import validate_comma_separated_integer_list

# Create your models here.
class UserOptions(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_first = models.BooleanField('是否首套', default=True)
    weight = models.CharField('权重', validators=[validate_comma_separated_integer_list], max_length=128, default='10,10,10,10,10,10,10,10,10,10')

class Area(models.Model):
    name = models.CharField('板块名称', max_length=128)

class Neighbor(models.Model):
    name = models.CharField('楼盘名称', max_length=128)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    address = models.CharField('地址', max_length=128)

class House(models.Model):
    neighbor = models.ForeignKey(Neighbor, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    square = models.DecimalField('面积', max_digits=8, decimal_places=2)
    rooms = models.CharField('房型', validators=[validate_comma_separated_integer_list], max_length=128)
    floor = models.CharField('楼层', validators=[validate_comma_separated_integer_list], max_length=8)
    age = models.IntegerField('年代')
    price = models.IntegerField('价格')
    tax_type = models.IntegerField('税费类型')
    lift_house = models.CharField('梯户比', validators=[validate_comma_separated_integer_list], max_length=8)
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
