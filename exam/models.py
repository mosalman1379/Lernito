from django.db import models
from lesson.models import Chapter


class Quiz(models.Model):
    chapters = models.ManyToManyField(to=Chapter, related_name='chapters')
    name = models.CharField(max_length=50, verbose_name='نام امتحان')
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return self.name


class Choices(models.TextChoices):
    first = ('1', '1'),
    second = ('2', '2'),
    third = ('3', '3'),
    fourth = ('4', '4')


class Question(models.Model):
    quiz = models.ForeignKey(to=Quiz,on_delete=models.PROTECT)
    question_name = models.TextField(verbose_name='صورت سوال')
    correct = models.CharField(max_length=10, choices=Choices.choices, default=Choices.first)


class Choice(models.Model):
    question = models.ForeignKey(to=Question, related_name='choices', on_delete=models.CASCADE)
    choice = models.CharField(max_length=50, verbose_name='گزینه سوال')
    position = models.PositiveSmallIntegerField(verbose_name='position')

    class Meta:
        unique_together = (
            ('question', 'choice'),
            ('question', 'position')
        )
        ordering = ('position',)
