from django.contrib import admin

from aadmin.models import Student, ClassRoom, Teacher
# Register your models here.

class ClassRoomAdmin(admin.ModelAdmin):
    pass

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass

class StudentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Student, StudentAdmin)
admin.site.register(ClassRoom, ClassRoomAdmin)
admin.site.register(Teacher, TeacherAdmin)

# admin.site.register(Student)
# admin.site.register(ClassRoom)
# admin.site.register(Teacher)

