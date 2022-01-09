from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin, GroupAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _
from users.models import AuthUser, Profile
from my_admin.admin import my_admin_site


class ProfileInline(admin.TabularInline):
    model = Profile
    extra = 3


# to display AUTHENTICATION AND AUTHORIZATION on the admin page
@admin.register(Group, site=my_admin_site)
class GroupAdmin(GroupAdmin):
    pass


@admin.register(AuthUser, site=my_admin_site)  # site is required if we have custom admin site
class AdminAuthUser(BaseUserAdmin):
    ordering = ('email',)
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active')
    search_fields = ('email', 'first_name', 'last_name')
    readonly_fields = ('date_joined', )
    actions = ('activate_users', 'deactivate_users', )
    inlines = (ProfileInline, )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name',)}),
        (_('Superuser section'), {
            'fields': ('is_superuser',),
        }),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    # Overriding the get_form method to limit changes in the admin page
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        disabled_fields = set()  # Initiating the set

        if not is_superuser:
            # updating the set in place
            disabled_fields |= {
                'email',
                # 'is_superuser',
                # 'user_permissions',
            }

        # Prevent non-superusers from editing their own permissions
        if not is_superuser and obj is not None and obj == request.user:
            disabled_fields |= {
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            }

        for field in disabled_fields:
            if field in form.base_fields:
                form.base_fields[field].disabled = True

        return form

    # prevent staff from deleting a model instance, regardless of their permissions
    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        else:
            return False

    @admin.action(description='Activate users')
    def activate_users(self, request, queryset):
        users = queryset.filter(is_active=False).update(is_active=True)
        self.message_user(request, f'Activated {users} users.')

    @admin.action(description='Deactivate users')
    def deactivate_users(self, request, queryset):
        users = queryset.filter(is_active=True).update(is_active=False)
        self.message_user(request, f'Deactivated {users} users.')

    # limit access to actions
    def get_actions(self, request):
        actions = super().get_actions(request)
        if not request.user.has_perm('auth.change_user'):
            actions_to_delete = ['activate_users']
            for action in actions_to_delete:
                del actions[action]

        return actions
