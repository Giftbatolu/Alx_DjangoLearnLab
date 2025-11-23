from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('title', 'author', 'publication_year')

    # Fields to filter by in the right-hand sidebar
    list_filter = ('author', 'publication_year')

    # Fields searchable from the search bar at the top
    search_fields = ('title', 'author')

class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'date_of_birth', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'date_of_birth', 'profile_picture')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'date_of_birth', 'profile_picture', 'password1', 'password2'),
        }),
    )
    search_fields = ('username', 'email')
    ordering = ('username', 'email')

admin.site.register(CustomUser, UserAdmin)