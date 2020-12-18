from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from apps.cart.models.models import Cart
# from apps.order.models.models import Order
from apps.users.models.profiles import Profile


# class OrderInline(admin.TabularInline):
#     model = Order
#     can_delete = False


class CartInline(admin.TabularInline):
    model = Cart
    can_delete = False


class ProfileInline(admin.StackedInline):
    inlines = (CartInline,)
    model = Profile
    can_delete = False


class CustomUserAdmin(UserAdmin):
    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

    inlines = (ProfileInline,)
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'is_staff',
    )


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)
