import strawberry
from gqlauth.user.queries import UserQueries, UserType
from gqlauth.user import arg_mutations as mutations

from .models import User


@strawberry.type
class Query(UserQueries):
    pass


@strawberry.django.type(model=User)
class MyQueries:
    active_user: UserType = UserQueries.me
    public_user: UserType = UserQueries.public_user


@strawberry.type
class Mutation:
    verify_token = mutations.VerifyToken.field
    update_account = mutations.UpdateAccount.field
    archive_account = mutations.ArchiveAccount.field
    delete_account = mutations.DeleteAccount.field
    password_change = mutations.PasswordChange.field
    token_auth = mutations.ObtainJSONWebToken.field
    register = mutations.Register.field
    verify_account = mutations.VerifyAccount.field
    resend_activation_email = mutations.ResendActivationEmail.field
    send_password_reset_email = mutations.SendPasswordResetEmail.field
    password_reset = mutations.PasswordReset.field
    password_set = mutations.PasswordSet.field
    refresh_token = mutations.RefreshToken.field
    revoke_token = mutations.RevokeToken.field
