import json


def cresponse(stats, message):
    response = {
        "stats": stats,
        "message": message
    }
    return json.dumps(response)
