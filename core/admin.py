from django.contrib import admin
from .models import Doctor, Patient,  TimesTable, Speciality, ReceptionTime


@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    pass


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    pass


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    pass


# @admin.register(WorkingHour)
# class WorkingHourAdmin(admin.ModelAdmin):
#     pass


@admin.register(ReceptionTime)
class ReceptionTime(admin.ModelAdmin):
    pass


@admin.register(TimesTable)
class TableTimeAdmin(admin.ModelAdmin):
    pass

# Register your models here.
