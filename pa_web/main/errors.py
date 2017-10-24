# Errors management
from flask import render_template, request, jsonify
from . import main

# *** NOTE *** this decorator create an application wide error management
#              the simple errorhandler will manage errors only in the blueprint
# The 404 and 500 errors are for all application
@main.app_errorhandler(404)
def page_not_found(e):
    if( request.accept_mimetypes.accept_json and \
        not request.accept_mimetypes.accept_html):
        response = jsonify({'error' : 'not found'})
        response.status_code = 404
        return response
    return render_template('404.html'), 404

@main.app_errorhandler(500)
def internal_server_error(e):
    if( request.accept_mimetypes.accept_json and \
        not request.accept_mimetypes.accept_html):
        response = jsonify({'error' : 'server error'})
        response.status_code = 500
        return response
    return render_template('500.html'), 500

