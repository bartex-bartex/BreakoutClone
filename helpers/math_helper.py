def calculate_center(width, object_length = 1) -> int:
    """
    Calculate x position at which the text should begin.

    :param int width: Display screen width
    :param int object_length: How long is displayed object
    :return int: x position 
    """
    if object_length < 1:
        raise Exception('Width should be >= 1')

    if object_length == 1:
        return int((width - 1) // 2)
    else:
        return int((width + 1) // 2 - (object_length // 2))
