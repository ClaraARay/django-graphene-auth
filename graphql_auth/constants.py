from django.utils.translation import gettext as _
import graphene
from uobtheatre.utils.exceptions import NonFieldError

class Messages(graphene.ObjectType):
    INVALID_PASSWORD = NonFieldError(message = _("Invalid password."), code ="invalid_password")
    UNAUTHENTICATED = NonFieldError(message = _("Unauthenticated."), code ="unauthenticated")
    INVALID_TOKEN = NonFieldError(message= _("Invalid token."), code="invalid_token")
    EXPIRED_TOKEN = NonFieldError(message = _("Expired token."), code ="expired_token")
    ALREADY_VERIFIED = NonFieldError(message = _("Account already verified."), code ="already_verified")
    EMAIL_FAIL = NonFieldError(message = _("Failed to send email."), code ="email_fail")
    INVALID_CREDENTIALS = NonFieldError(message = _("Please, enter valid credentials."),
        code ="invalid_credentials",
    )
    NOT_VERIFIED = NonFieldError(message = _("Please verify your account."), code ="not_verified")
    NOT_VERIFIED_PASSWORD_RESET = NonFieldError(message = _("Verify your account first. A new verification email was sent."),
        code ="not_verified",
    )
    EMAIL_IN_USE =  NonFieldError(message= _("A user with that email already exists."), code ="email_in_use")
    SECONDARY_EMAIL_REQUIRED = NonFieldError(message = _("You need to setup a secondary email to proceed."),
        code ="secondary_email_required",
    )
    PASSWORD_ALREADY_SET = NonFieldError(message = _("Password already set for account."),
        code ="password_already_set",
    )
    INVALID_REGISTRATION_DATA = NonFieldError(message = _("Invalid registration data."),
        code ='invalid_registration_data',
    )
    FAILED_SENDING_ACTIVATION_EMAIL = NonFieldError(message = _("User account created but could not send activation email."),
        code ='send_activation_email_failed',
    )
    FAILED_PASSWORD_CHANGE = NonFieldError(message = _("Password change failed."),
        code ='password_change_failed',
    )
    INVALID_EMAIL_ADDRESS = NonFieldError(message = _("Invalid email address."),
        code ='invalid_email_address',
    )


class TokenAction(object):
    ACTIVATION = "activation"
    PASSWORD_RESET = "password_reset"
    ACTIVATION_SECONDARY_EMAIL = "activation_secondary_email"
    PASSWORD_SET = "password_set"
