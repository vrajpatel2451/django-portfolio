def seriliaze(data,success,error):
    if success:
        return {"success":True, "data":data}
    if error:
        return {"success":False, "errors":data}