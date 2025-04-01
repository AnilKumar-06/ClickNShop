from django.contrib.auth.backends import BaseBackend
from accounts.models import Accounts  # Your custom user model

class EmailAuthBackend(BaseBackend):
    """Authenticate using email instead of username"""
    
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Accounts.objects.get(email=username)  # Get user by email
            if user.check_password(password):  # Check password
                return user
        except Accounts.DoesNotExist:
            return None
        return None
    
    def get_user(self, user_id):
        try:
            return Accounts.objects.get(pk=user_id)
        except Accounts.DoesNotExist:
            return None

