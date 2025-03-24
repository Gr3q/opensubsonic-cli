import enum
from pydantic import BaseModel

class SubsonicErrorCode(enum.IntEnum):
    GENERIC = 0
    ''' 	A generic error.'''
    PARAM_MISSING = 10
    ''' 	Required parameter is missing.'''
    OLD_CLIENT_PROTOCOL = 20
    ''' 	Incompatible Subsonic REST protocol version. Client must upgrade.'''
    OLD_SERVER_PROTOCOL = 30
    ''' 	Incompatible Subsonic REST protocol version. Server must upgrade.'''
    INVALID_AUTH_DETAILS = 40
    ''' 	Wrong username or password.'''
    TOKEN_LDAP_AUTH_UNSUPPORTED = 41
    ''' 	Token authentication not supported for LDAP users.'''
    AUTH_MECHANISM_UNSUPPORTED = 42
    ''' 	Provided authentication mechanism not supported.'''
    MULTIPLE_AUTH_MECHANISM_PROVIDED = 43
    ''' 	Multiple conflicting authentication mechanisms provided.'''
    INVALID_API_LEY = 44
    ''' 	Invalid API key.'''
    NOT_AUTHORIZED = 50
    ''' 	User is not authorized for the given operation.'''
    TRIAL_EXPIRED = 60
    ''' 	The trial period for the Subsonic server is over. Please upgrade to Subsonic Premium. Visit subsonic.org for details.'''
    NOT_FOUND = 70
    ''' 	The requested data was not found.'''

class SubsonicError(BaseModel):
    code: SubsonicErrorCode
    '''The error code'''
    message: str | None = None
    '''The optional error message'''
    helpUrl: str | None = None
    '''A URL (documentation, configuration, etc) which may provide additional context for the error)'''