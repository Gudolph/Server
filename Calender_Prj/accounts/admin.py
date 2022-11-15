from django.contrib import admin
from django.contrib.auth.models import User
# Register your models here.

# @admin.register(User) # admin 페이지에 넣을 모델
# class UserAdmin(admin.ModelAdmin):
#     list_display = "__all__"
#     # list_display = ('id','username','realName') # admin에 출력되는 리스트
#     # list_display_links = ['id','username','realName'] # 링크 달기
#     # list_filter = ['date_joined'] # admin창 오른쪽에 필터 생김
#     search_fields = ['username'] # 검색창 만들기
