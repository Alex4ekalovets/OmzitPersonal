from django.contrib import admin

from timesheet.models import Employee, Timesheet, DayStatus


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    all_fields = [
        "fio",
        "employment_date",
        "fired_date",
        "job_title",
        "rank_title",
        "tariff_rate",
        "id_1C",
        "division",
        "status",
        "schedule",
        "shift_hours",
        "skud_access",
        "day_start",
        "boss",
        "KTR_category",
        "KTR",
        "has_NAX",
        "KNAX",
    ]
    list_display = all_fields
    list_display_links = ["fio"]
    search_fields = ["fio"]
    list_filter = [
        "job_title",
        "rank_title",
        "division",
        "status",
        "schedule",
        "shift_hours",
        "skud_access",
        "day_start",
        "boss",
        "KTR_category",
        "has_NAX",
    ]
    list_editable = [
        "status",
        "schedule",
        "shift_hours",
        "skud_access",
        "day_start",
        "boss",
        "KTR_category",
        "KTR",
        "has_NAX",
        "KNAX"
    ]


@admin.register(Timesheet)
class TimesheetAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            None,
            {
                "fields": [
                    "fio",
                    "day_status",
                    "date",
                ],
            },
        ),
        (
            "Дневная смена",
            {
                "fields": [
                    "skud_day_start_1",
                    "skud_day_end_1",
                    "skud_day_start_2",
                    "skud_day_end_2",
                    "skud_day_duration",
                    "boss_day_duration",
                    "is_day_corrected",
                ],
                "classes": ["collapse"],
            },
        ),
        (
            "Ночная смена",
            {
                "fields": [
                    "skud_night_start_1",
                    "skud_night_end_1",
                    "skud_night_start_2",
                    "skud_night_end_2",
                    "skud_night_duration",
                    "boss_night_duration",
                    "is_night_corrected",
                ],
                "classes": ["collapse"],
            },
        ),
    ]
    list_display = [
        "fio",
        "day_status",
        "date",
        "skud_day_start_1",
        "skud_day_end_1",
        "skud_day_start_2",
        "skud_day_end_2",
        "skud_day_duration",
        "boss_day_duration",
        "is_day_corrected",
        "skud_night_start_1",
        "skud_night_end_1",
        "skud_night_start_2",
        "skud_night_end_2",
        "skud_night_duration",
        "boss_night_duration",
        "is_night_corrected",
    ]
    list_display_links = ["fio"]
    search_fields = ["fio"]
    list_filter = [
        "fio",
        "day_status",
        "date",
        "skud_day_duration",
        "boss_day_duration",
        "skud_night_duration",
        "boss_night_duration",
        "is_day_corrected",
        "is_night_corrected",
    ]
    list_editable = [
        "boss_day_duration",
        "boss_night_duration",
    ]


@admin.register(DayStatus)
class DayStatusAdmin(admin.ModelAdmin):
    list_display = ["symbol", "name"]
    list_display_links = ["symbol"]
    search_fields = ["symbol", "name"]
