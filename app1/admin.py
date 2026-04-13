from django.contrib import admin

from app1.models import students,deparments,faculty
# Register your models here.

class studens_admin(admin.ModelAdmin):
    list_display=['std_id','std_name','std_dept']
admin.site.register(students,studens_admin)


class dept_admin(admin.ModelAdmin):
    list_display=['dept_name','dept_name']
admin.site.register(deparments,dept_admin)


class faculty_admin(admin.ModelAdmin):
    list_display=['faculty_id','faculty_name']
admin.site.register(faculty,faculty_admin)