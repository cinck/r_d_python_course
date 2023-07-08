import werkzeug.exceptions as r_errors
from app import app

# <HW33> Task 5. Custom error handlers for errors 404, 500.


@app.errorhandler(r_errors.NotFound)
def handle_not_found(error):
    """
    Error 404 handler
    :param error:
    :return:
    """
    response = f"""
        <h1>Bad luck! Sorry! Can't find it anywhere... </h1>
        <h3>{error}. Are you sure you need it?</h3>
    """
    return response, 404


@app.errorhandler(r_errors.InternalServerError)
def handle_internal_server_error(error):
    """
    Error 500 handler
    :param error:
    :return:
    """
    response = f"""
        <h1>Oh, shit! Me apologize!</h1>
        <h3>{error}. That shouldn't be like that.</h3>
    """
    return response, 500
