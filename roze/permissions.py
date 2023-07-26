from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):

    message = "you can't edit this roze object , you are not the owner !!"
    def has_object_permission(self, request, view, obj):

        if request.method == 'GET':
            return True

        if request.user == obj.owner :
            return True
        else :
            return False
        # if request.method == 'GET':
        #     return True
        # return request.user == obj.owner