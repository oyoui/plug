from django.urls import reverse
from django.utils.safestring import mark_safe

from app01 import models
from yingun.service import v1


class YinGunUserInfo(v1.BaseYinGunAdmin):


    def func(self, obj=None,is_header=False):
        if is_header:
            return "操作"
        else:

            from django.http.request import QueryDict
            param_dict = QueryDict(mutable=True)
            if self.request.GET:
                param_dict['_changelistfilter'] = self.request.GET.urlencode()

            base_edit_url = reverse("{2}:{0}_{1}_change".format(self.app_lable, self.model_name, self.site.namespace),
                                    args=(obj.pk,))
            #print(base_edit_url)
            edit_url = "{0}?{1}".format(base_edit_url, param_dict.urlencode())

            return mark_safe("<a href='{0}'>编辑</a>".format(edit_url))

    def checkbox(self,obj=None,is_header=False):
        if is_header:
            return "选项"
        else:
            tag = "<input name='pk' type='checkbox' value='{0}'/>".format(obj.pk)
            return mark_safe(tag)

    def comb(self,obj=None,is_header=False):
        if is_header:
            return "复合列"
        else:
            return "%s-%s" %(obj.username,obj.email)

    list_display = [checkbox,'id','username','email',comb,func]

    #### 动作
    def initial(self,request):
        pk_list = request.POST.getlist('pk')
        models.UserInfo.objects.filter(pk__in=pk_list).update(username="于浩")
        return True

    initial.text = "初始化"

    def multi_del(self,request):
        pass
    multi_del.text = "批量删除"

    action_list = [initial,multi_del]


    #### 组合搜索

    from yingun.utils.filter_code import FilterOption
    filter_list = [
        FilterOption('username',False),
        FilterOption('ug',False),
        FilterOption('m2m',False)
    ]



v1.site.register(models.UserInfo,YinGunUserInfo)




class YinGunRole(v1.BaseYinGunAdmin):
    list_display = ['id','name']

v1.site.register(models.Role,YinGunRole)


class YinGunUserGroup(v1.BaseYinGunAdmin):
    list_display = ['title']

v1.site.register(models.UserGroup,YinGunUserGroup)