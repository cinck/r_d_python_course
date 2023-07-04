import werkzeug.exceptions as r_errors
from app import app


@app.errorhandler(r_errors.NotFound)
def handle_not_found(e):
    return "Can't find it anywhere... Are you sure you need it?", 404


@app.errorhandler(r_errors.InternalServerError)
def handle_internal_server_error(e):
    return "Oh, shit! That shouldn't be like that. Sorry!", 500
