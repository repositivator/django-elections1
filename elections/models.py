from django.db import models

# Create your models here.

class Candidate(models.Model):      # 클래스 이름은 단수형으로 적어주는 게 일반적, models.py 의 Model 클래스를 상속받음
    name = models.CharField(max_length=10)
    introduction = models.TextField()   # 길이제한 없음
    area = models.CharField(max_length=15)
    party_number = models.IntegerField(default=0)   # 후보번호 디폴트값 0으로 지정

    def __str__(self):
        return self.name


class Poll(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    area = models.CharField(max_length=15)

    def __str__(self):
        return self.area + str(self.id)

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    candidate = models.ForeignKey(Candidate)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id) + self.candidate.name
