from django.contrib import admin
from .models import TodoList, Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'todolist', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('status', 'todolist', 'created_at')

    

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(todolist__creator=request.user)

    def has_change_permission(self, request, obj=None):
        if obj is None:
            return True
        return obj.todolist.creator == request.user or request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        if obj is None:
            return True
        return obj.todolist.creator == request.user or request.user.is_superuser
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "todolist":
            kwargs["queryset"] = TodoList.objects.filter(creator=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
  

class TodoListAdmin(admin.ModelAdmin):
    list_display = ('title', 'creator', 'created_at')
    search_fields = ('title', 'creator__username')
    list_filter = ('creator', 'created_at')

    exclude = ('creator',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(creator=request.user)

    def has_change_permission(self, request, obj=None):
        if obj is None:
            return True
        return obj.creator == request.user or request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        if obj is None:
            return True
        return obj.creator == request.user or request.user.is_superuser

    def save_model(self, request, obj,  change):
        if not change or not obj.creator:
            obj.creator = request.user
        obj.save()

    def save_model(self, request, obj, form, change):
        if not change or not obj.creator:
            obj.creator = request.user
        obj.save()

admin.site.register(TodoList, TodoListAdmin)
admin.site.register(Task, TaskAdmin)
