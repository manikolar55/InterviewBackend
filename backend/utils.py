from rest_framework.response import Response


def json_response(success=False, message='', data=None, status=200):
    """
    Create json response in a specifc format

    Parameters
    ----------
    success : bool, optional
        request success status
    message : str, optional
        response message if any
    data : dict, optional
        response body if any
    status : int, optional
        response status

    Returns
    -------
    rest_framework.response.Response
    """
    return Response({"success": success,
                     "message": message,
                     "data": data}, status=status)
