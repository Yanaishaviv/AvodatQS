import constants 

def list_nums(message):
    tmp_msg = message[1:-1]
    ret_me = tmp_msg.split(constants.SEPARATOR)
    return ret_me


def parse_string_data(message):
    nums = list_nums(message)
    readable_data = []
    for num in nums:
        readable_data.append(int(num))
    return readable_data

