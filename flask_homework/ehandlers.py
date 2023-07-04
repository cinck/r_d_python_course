import werkzeug.exceptions as r_errors
from app import app


@app.errorhandler(r_errors.NotFound)
def handle_not_found(e):
    response = """
        <h1>Bad luck! Sorry!</h1>
        <h3>Can't find it anywhere... Are you sure you need it?</h3>
    """
    return response, 404


@app.errorhandler(r_errors.InternalServerError)
def handle_internal_server_error(e):
    response = """
        <h1>Oh, shit! Me apologize!</h1>
        <h3>That shouldn't be like that.</h3>
    """
    return response, 500
