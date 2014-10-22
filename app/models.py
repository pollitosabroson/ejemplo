from django.db import models

#Create your models here.
# class Client(models.Model):
#     class Meta:
#         verbose_name = "Client"
#         verbose_name_plural = "Clients"
#         ordering = ['name']

#     name = models.CharField(u'Nombre', max_length= 50, null = False)
#     lastname = models.CharField(u'Apellidos', max_length= 50, null = True)
#     description = models.TextField(u'Extras', null = False, blank=True)
#     create = models.DateTimeField(auto_now=True, null=True, blank=True)

#     def __unicode__(self):
#         return u'%s'%self.name
        
#     def last(self):
#     	return self.school_set.all()
    
# class School(models.Model):
#     class Meta:
#         verbose_name = "School"
#         verbose_name_plural = "School"
#         unique_together = (("nameSchool", "like"),)

#     types = (
#     		('Elementary','Elementary'),
#         	('High School','High School'),
#         	('University','University'),
#         )
#     nameSchool = models.CharField(u'Nombre de la escuela',max_length= 50, null=False, blank=False)
#     name = models.ForeignKey(Client, null = False, verbose_name='Nombre del alumno')
#     like = models.CharField(u'tipo de escuela',max_length= 50, choices=types)


#     def __unicode__(self):
#         return u'%s'%self.nameSchool