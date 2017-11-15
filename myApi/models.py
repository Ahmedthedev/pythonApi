from django.db import models


class Professor(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)

    def __str__(self):
        return super().__str__()

    class Meta:
        unique_together = ('firstname','lastname')



class Subject(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    fk_subject_professor = models.ForeignKey(
        'Subject',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return super().__str__()

    class Meta:
        unique_together = ('code','name')

class Classe(models.Model):
    date = models.DateTimeField()
    duration = models.IntegerField()
    fk_classe_subject = models.ForeignKey(
        'Subject',
        on_delete=models.CASCADE,
    )

    class Meta:
        unique_together = ('date','duration','fk_classe_subject')

    def __str__(self):
        return super().__str__()

class Promotion(models.Model):
        code = models.CharField(max_length=5)
        duration = models.CharField(max_length=50)
        fk_promotion_classe = models.ForeignKey(
            'Classe',
            on_delete=models.CASCADE,
        )

        class Meta:
            unique_together = ('code', 'duration', 'fk_promotion_classe')


        def __str__(self):
            return super().__str__()

class SubjectPromotionFk(models.Model):
    fk_subjectpromotionfk_subject = models.ForeignKey(
        'Subject',
        on_delete=models.CASCADE,
    )
    fk_subjectpromotionfk_promotion = models.ForeignKey(
        'Promotion',
        on_delete=models.CASCADE,
    )

    class Meta:
        unique_together = ('fk_subjectpromotionfk_subject', 'fk_subjectpromotionfk_promotion')

    def __str__(self):
        return super().__str__()


class Student(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    fk_student_classe = models.ForeignKey(
        'Classe',
        on_delete=models.CASCADE,
    )

    class Meta:
        unique_together = ('firstname', 'lastname','fk_student_classe')


    def __str__(self):
        return super().__str__()

