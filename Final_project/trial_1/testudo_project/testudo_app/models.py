from django.db import models
import json

class CourseList(models.Model):
    course_id=models.CharField(max_length=50)
    name=models.CharField(max_length=100)

class CourseInfo(models.Model):
    course_id=models.CharField(max_length=50)
    semester=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    dept_id=models.CharField(max_length=50)
    department=models.CharField(max_length=50)
    credits=models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    grading_method=models.CharField(max_length=200)
    gen_ed=models.CharField(max_length=200)
    core=models.CharField(max_length=50)
    relationships=models.CharField(max_length=1000)
    sections=models.CharField(max_length=1000)

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
