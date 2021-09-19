from django.db import models
from django_jalali.db import models as jalali
from taggit.managers import TaggableManager


class Book(models.Model):
    """
    Describe each lesson book model (class) fields
    """

    # inner class for describe degree
    class Degrees(models.TextChoices):
        elementary = ('1', 'دبستان'),
        first_HighSchool = ('2', 'متوسطه اول'),
        second_HighSchool = ('3', 'متوسطه دوم')

    # inner class for describe grade
    class Grade(models.TextChoices):
        first = ('1', 'اول'),
        second = ('2', 'دوم'),
        third = ('3', 'سوم'),
        fourth = ('4', 'چهارم'),
        fifth = ('5', 'پنجم'),
        sixth = ('6', 'ششم'),
        seventh = ('7', 'هفتم'),
        eighth = ('8', 'هشتم'),
        ninth = ('9', 'نهم'),
        tenth = ('10', 'دهم'),
        eleventh = ('11', 'یازدهم'),
        twelfth = ('12', 'دوازدهم')

    # inner class for describe study field
    class StudyField(models.TextChoices):
        math = ('math', 'ریاضی'),
        Experimental = ('experimental', 'تجربی'),
        Humanities = ('humanities', 'انسانی')

    name = models.CharField(max_length=100, verbose_name='نام درس')
    section = models.CharField(choices=Degrees.choices, max_length=30,verbose_name='مقطع تحصیلی')
    grade = models.CharField(choices=Grade.choices, max_length=30, verbose_name='پایه تحصیلی')
    study_field = models.CharField(choices=StudyField.choices, max_length=30,verbose_name='رشته تحصیلی')
    publication_date = jalali.jDateTimeField(verbose_name='تاریخ نشر')
    publisher = models.CharField(max_length=150, verbose_name='ناشر')
    pdf = models.FileField(upload_to='books/', verbose_name='فایل کتاب')
    image = models.ImageField(upload_to='images/', verbose_name='عکس کتاب')
    page = models.PositiveIntegerField(verbose_name='تعداد صفحات کتاب',default=1)
    # create tags for getting recommended books
    tag = TaggableManager()

    def __str__(self):
        return f'{self.name} of {self.grade}'

    def lesson_chapter_count(self):
        return self.chapter_set.all().count()


class Chapter(models.Model):
    """
    Chapter description
    """
    name = models.CharField(max_length=80,verbose_name='نام فصل')
    # each chapter belong to a book
    lesson = models.ForeignKey(to=Book,on_delete=models.PROTECT)
    number = models.PositiveSmallIntegerField(verbose_name='شماره فصل')

    def __str__(self):
        return f'{self.name} of {self.lesson}'

    class Meta:
        ordering = ('number',)


