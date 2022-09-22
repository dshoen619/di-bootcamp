from django.db import models
import json


class CourseList(models.Model):
    course_id=models.CharField(max_length=50)
    name=models.CharField(max_length=500)

class CourseInfo(models.Model):
    course_id=models.CharField(max_length=500)
    semester=models.CharField(max_length=500,null=True, blank=True)
    name=models.CharField(max_length=500, null=True, blank=True)
    dept_id=models.CharField(max_length=500, null=True, blank=True)
    department=models.CharField(max_length=500, null=True, blank=True)
    credits=models.CharField(max_length=500, null=True, blank=True)
    description = models.CharField(max_length=3000, null=True, blank=True)
    grading_method=models.CharField(max_length=1000, null=True, blank=True)
    gen_ed=models.CharField(max_length=1000, null=True, blank=True)
    core=models.CharField(max_length=1000, null=True, blank=True)
    relationships=models.CharField(max_length=3000, null=True, blank=True)
    sections=models.CharField(max_length=3000, null=True, blank=True)

    def set_grading_method(self,x):
        self.grading_method=json.dumps(x)

    def set_gen_ed(self,x):
        self.gen_ed=json.dumps(x)

    def set_core(self,x):
        self.core=json.dumps(x)

    def set_relationship(self,x):
        self.relationships=json.dumps(x)

    def set_sections(self,x):
        self.sections=json.dumps(x)

class Professors(models.Model):
    name= models.CharField(max_length=100)
    course_id=models.CharField(max_length=5000)

class SavedCourses(models.Model):
    username = models.CharField(max_length=50)
    course_id=models.CharField(max_length=500)
    semester=models.CharField(max_length=500,null=True, blank=True)
    name=models.CharField(max_length=500, null=True, blank=True)
    dept_id=models.CharField(max_length=500, null=True, blank=True)
    department=models.CharField(max_length=500, null=True, blank=True)
    credits=models.CharField(max_length=500, null=True, blank=True)
    description = models.CharField(max_length=3000, null=True, blank=True)
    grading_method=models.CharField(max_length=1000, null=True, blank=True)
    gen_ed=models.CharField(max_length=1000, null=True, blank=True)
    core=models.CharField(max_length=1000, null=True, blank=True)
    relationships=models.CharField(max_length=3000, null=True, blank=True)
    sections=models.CharField(max_length=3000, null=True, blank=True)
    a=models.CharField(max_length=40,null=True, blank=True)
    
class UserSavedCourses(models.Model):
    username = models.CharField(max_length=50)
    course_id=models.CharField(max_length=500)
    semester=models.CharField(max_length=500,null=True, blank=True)
    name=models.CharField(max_length=500, null=True, blank=True)
    dept_id=models.CharField(max_length=500, null=True, blank=True)
    department=models.CharField(max_length=500, null=True, blank=True)
    credits=models.CharField(max_length=500, null=True, blank=True)
    description = models.CharField(max_length=3000, null=True, blank=True)
    grading_method=models.CharField(max_length=1000, null=True, blank=True)
    gen_ed=models.CharField(max_length=1000, null=True, blank=True)
    core=models.CharField(max_length=1000, null=True, blank=True)
    relationships=models.CharField(max_length=3000, null=True, blank=True)
    sections=models.CharField(max_length=3000, null=True, blank=True)




