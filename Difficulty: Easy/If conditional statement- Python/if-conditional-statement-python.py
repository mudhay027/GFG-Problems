def friends_in_trouble(j_angry, s_angry):
    if j_angry and s_angry:
        return True
    elif j_angry or s_angry:
        return False
    else:
        return True