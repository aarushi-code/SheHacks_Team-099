from django.contrib import admin
from accounts.models import Account
from django.contrib.auth.admin import UserAdmin
from .forms import SignUpForm, MyUserChangeForm


# Register your models here.

# admin.site.register(Account)

# class CustomUserAdmin(UserAdmin):
#     add_form = SignUpForm
#     form = MyUserChangeForm

#     fieldsets = UserAdmin.fieldsets + (
#             (None, {'fields': ('some_extra_data',)}),
#             list_display = ('email', 'is_staff', 'is_active',)
#             list_filter = ('email', 'is_staff', 'is_active',)
#     )


class CustomUserAdmin(UserAdmin):
    add_form = SignUpForm
    form = MyUserChangeForm
    model = Account
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    readonly_fields = ("reg_date",)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_admin', 'is_superuser')}),
        ('Personal Info', {'fields': ('name', 'mobile', 'Class', 'Board', 'username', 'Course', 'Mentorship', 'Payment')}),

    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'mobile', 'Class', 'Board', 'username', 'Course', 'Mentorship', 'Payment')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(Account, CustomUserAdmin)