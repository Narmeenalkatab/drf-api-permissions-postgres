from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):

    message = "you cant edit this Snack object , you are not the owner !!"
    
    def has_object_permission(self, request, view, obj):

        if request.method == 'GET':
            return True
        
        if request.user == obj.owner :
            return True 
        else : 
            return False 
       