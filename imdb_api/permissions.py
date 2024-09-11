from rest_framework import permissions 

class AdminOrReadOnly(permissions.IsAdminUser): 
    message = "Admin or read only." 

    def has_permissions(self, request, view):
        admin_permission =  super().has_permission(request=request, view=view) 
        if request.method == 'GET' or admin_permission: 
            return True  
        return False       