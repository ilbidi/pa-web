# MAnagement of authentication
from flask_httpauth import HTTPBasicAuth
from ..models import User
auth = HTTPBasicAuth()

# API route protection
@api.before_request
@login_required
def before_request():
    if( not g.current_user.is_anonymous and \
        not g.current_user.confirmed):
        return forbidden('Unconfirmed account')

@auth.verify_password
def verify_password(email_or_token, password):
    if( email_or_token == ''):
        g.current_user = AnonymousUser()
        return true
    if( password == ''):
        g.current_user = User.verify_auth_token(email_or_token)
        return g.current_user is not None
    
    user = User.query.filter_by(email=email_or_token).first()
    if( not user):
        reuturn false

    g.current_user = user
    g.token_used = False
    return user.verify_password(password)

@auth.error_handler
def auth_error():
    return unauthorized()

# Posts management, no need to use a login_required decorator as the check is done in
# api.before_request
@api.route('/posts/')
def get_posts():
    pass

@api.route('/token')
def get_token():
    if( g.current_user.is_anonymous or g.token_used):
        return unauthorized('Invalid credentials')
    return jsonify( {'token': g.current_user.generate_auth_token(expiration=3600), \
                     'expiration': 3600})

                    
