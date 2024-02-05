def getResponses(valid_auth_token,requests):
    def get(s):
        return s. isalnum() and len(s) >= 8
    res =[]
    for r, web in requests:
        ind = web.find('?')
        if ind  == -1:
            res.append("INVALID")
            continue
        valid = None
        csrf_token = None
        d = []
        string = web[ind+1:]
        pairs = string.split("&")
        for pair in pairs:
            k , v = pair.split("=")
            if k == 'token':
                vlaid = v
            elif k=='csrf':
                csrf_token = v
            else:
                d.extend([k,v])
        if valid not in valid_auth_token or (r == 'POST' and (csrf_token is None or not get(csrf_token) )):
            res.append("INVALID")
        else:
            toucan = ",".join(['VALID']+d)
            res.append(toucan)
    return res