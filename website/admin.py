from django.contrib import admin

from website.models import Student, ClassRoom


class StudentAdmin(admin.ModelAdmin):
    list_display = ('get_name', 'birth_date', 'email')


admin.site.register(Student, StudentAdmin)
admin.site.register(ClassRoom)
