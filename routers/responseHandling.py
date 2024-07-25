def success(message):
    return {
        "status": 200,
        "message": message
    }


def errorIncorrectParameter(message):
    return {
        "status": 480,
        "message": message
    }


def errorIncorrectMethod(message):
    return {
        "status": 481,
        "message": message
    }


def errorIDNotPresent(message):
    return {
        "status": 482,
        "message": message
    }


def errorIDAlreadyExists(message):
    return {
        "status": 483,
        "message": message
    }


def errorWrongFormatBody(message):
    return {
        "status": 484,
        "message": message
    }
