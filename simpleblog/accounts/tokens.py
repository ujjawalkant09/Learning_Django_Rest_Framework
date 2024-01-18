from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model

User = get_user_model()

def create_jwt_pair_for_user(user:User):
    referesh = RefreshToken.for_user(user)

    tokens = {
        "access": str(referesh.access_token),
        "refresh": str(referesh)
    }

    return tokens