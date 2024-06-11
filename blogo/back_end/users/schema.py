import strawberry
from gqlauth.user.queries import UserQueries, UserType
from gqlauth.core.middlewares import JwtSchema
from gqlauth.user import arg_mutations as mutations

from .models import User


@strawberry.type
class Query(UserQueries):
    pass


@strawberry.django.type(model=User)
class MyQueries:
    current_user: UserType = UserQueries.me
    public_user: UserType = UserQueries.public_user


@strawberry.type
class Mutation:
    register = mutations.Register.field
    verify_account = mutations.VerifyAccount.field
    resend_activation_email = mutations.ResendActivationEmail.field
    send_password_reset_email = mutations.SendPasswordResetEmail.field
    password_reset = mutations.PasswordReset.field
    password_set = mutations.PasswordSet.field
    refresh_token = mutations.RefreshToken.field
    token_auth = mutations.ObtainJSONWebToken.field


schema = JwtSchema(query=Query, mutation=Mutation)
