import json


def get_api_key(client, scopes=None):
    """
    Args:
        client: client fixture

    Return:
        pytest_flask.plugin.JSONResponse: the response from /oauth2/authorize
    """
    path = (
        '/credentials/cdis/'
    )
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    if scopes is None:
        scopes = ['data', 'user']
    response = client.post(path, data={'scopes': scopes}, headers=headers)
    return response


def get_api_key_with_json(client):
    """
    Args:
        client: client fixture

    Return:
        pytest_flask.plugin.JSONResponse: the response from /oauth2/authorize
    """
    path = (
        '/credentials/cdis/'
    )
    headers = {
        'Content-Type': 'application/json'
    }
    response = client.post(path, data=json.dumps({'scopes': ['data', 'user']}), headers=headers)
    return response
