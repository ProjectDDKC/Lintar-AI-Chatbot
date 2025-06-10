from save import save

def getsave(username):
    save.loader["username"] = username
    save.save()