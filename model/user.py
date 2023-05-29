
def user_info (user_fetch_one) :
    if user_fetch_one is None :
        return {}
    user_info = {}
    user_info['id'] = user_fetch_one[0]
    user_info['username'] = user_fetch_one[1]
    user_info['password'] = user_fetch_one[2]
    return user_info