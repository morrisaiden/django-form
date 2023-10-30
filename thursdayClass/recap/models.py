from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    classroom_number = models.IntegerField(default=(3))
    recording_number = models.IntegerField(default=(2))

    def __str__(self):
        return f"{self.name}: classroom {self.classroom_number} on age{self.age}"


class Schedule(models.Model):
    topic = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=(2))
    classroom = models.ForeignKey(Person, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.topic} - {self.date} - {self.start_time} - {self.classroom}"
