def user_info(user_fetch_one):
    if user_fetch_one is None:
        return {}
    user_info = {'id': user_fetch_one[0], 'username': user_fetch_one[1], 'password': user_fetch_one[2]}
    return user_info
