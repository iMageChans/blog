from django.contrib import admin
from main.models import Main, Simple
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.models import User, Group

admin.site.site_title = "PickMe统计后台"
admin.site.site_header = "PickMe统计后台"
admin.site.index_title = "PickMe统计后台"


class SimpleAdmin(admin.ModelAdmin):
    list_display = ['memberAdd',
                    'activeUsers',
                    'quantityPaid',
                    'totalRecharge',
                    ]

    list_per_page = 30

    # List_display_links = None  # 禁用编辑链接
    #
    # def has_add_permission(self, request):
    #     # 禁用添加按钮
    #     return False
    #
    # def has_delete_permission(self, request, obj=None):
    #     # 禁用删除按钮
    #     return False
    #
    # def has_change_permission(self, request, obj=None):
    #     return False
    #
    # def get_actions(self, request):
    #     # 在actions中去掉‘删除'操作
    #     actions = super(SimpleAdmin, self).get_actions(request)
    #     if request.user.username[0].upper() != 'J':
    #         if 'delete_selected' in actions:
    #             del actions['delete_selected']
    #     return actions

    class Meta:
        model = Simple

admin.site.register(Simple, SimpleAdmin)


class MainAdmin(admin.ModelAdmin):

    list_per_page = 30

    list_display = ['dateTime',
                    'regMember',
                    'toDayActivity',
                    'memberToDayActivity',
                    'memberQuantityPaid',
                    'totalMemberPayments',
                    'candyPaymentQuantity',
                    'totalCandyPayment',
                    'memberConversionRate',
                    'candyConversion',
                    ]

    List_display_links = None  # 禁用编辑链接

    def has_add_permission(self, request):
        # 禁用添加按钮
        return False

    def has_delete_permission(self, request, obj=None):
        # 禁用删除按钮
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def get_actions(self, request):
        # 在actions中去掉‘删除'操作
        actions = super(MainAdmin, self).get_actions(request)
        if request.user.username[0].upper() != 'J':
            if 'delete_selected' in actions:
                del actions['delete_selected']
        return actions

    class Meta:
        model = Main

admin.site.register(Main, MainAdmin)


class UserAdmin(BaseUserAdmin):

    def has_add_permission(self, request):
        # 禁用添加按钮
        return False

    def has_delete_permission(self, request, obj=None):
        # 禁用删除按钮
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def get_actions(self, request):
        # 在actions中去掉‘删除'操作
        actions = super(UserAdmin, self).get_actions(request)
        if request.user.username[0].upper() != 'J':
            if 'delete_selected' in actions:
                del actions['delete_selected']
        return actions

    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


admin.site.unregister(User)
admin.site.register(User, UserAdmin)


class GroupsAdmin(GroupAdmin):

    def has_add_permission(self, request):
        # 禁用添加按钮
        return False

    def has_delete_permission(self, request, obj=None):
        # 禁用删除按钮
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def get_actions(self, request):
        # 在actions中去掉‘删除'操作
        actions = super(GroupsAdmin, self).get_actions(request)
        if request.user.username[0].upper() != 'J':
            if 'delete_selected' in actions:
                del actions['delete_selected']
        return actions

    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


admin.site.unregister(Group)
admin.site.register(Group, GroupsAdmin)
