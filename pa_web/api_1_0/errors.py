# API errors management
# Errors 404 and 500 are implemented directly in main/errors.py as this part will manage both
# HTTP and json errors
# We will implement those messages
# 400 - bad request
# 401 - Unathorized
# 403 - Forbidden
# 405 - Method not allowed
from pa_web.exceptions import ValidationError

def bad_request(message):
    """Response to a 400 error - bad request"""
    response = jsonify({'error': 'bad_request', 'message': message})
    response.status_code = 400
    return response

def unauthorized(message):
    """Response to a 401 error - unauthorized"""
    response = jsonify({'error': 'unauthorized', 'message': message})
    response.status_code = 401
    return response

def forbidden(message):
    """Response to a 403 error - forbidden"""
    response = jsonify({'error': 'forbidden', 'message': message})
    response.status_code = 403
    return response

def method_not_allowed(message):
    """Response to a 405 error - method not allowed"""
    response = jsonify({'error': 'method_not_allowed', 'message': message})
    response.status_code = 405
    return response

# Global exception catcher for validation error
@api.errorhandler(ValidationError)
def validation_error(e):
    return bad_request(e.args[0])
