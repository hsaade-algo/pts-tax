def format_validation_error(error):
    filtered_errors = [
        {"field": err["loc"][0], "message": err["msg"], "type": err["type"]}
        for err in error.errors()
    ]
    return filtered_errors
