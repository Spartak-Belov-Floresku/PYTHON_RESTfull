import urllib.request

from src.db_layer import ProcessData


class GetData():
    def __init__(self, url):
        self.__url = url
        self.__SendRequest()


    def __SendRequest(self):
        try:
            with urllib.request.urlopen(self.__url) as responce:
                ProcessData(responce)
        except Exception as e:
            err = str(e)
            print("Business layer error :", err)
            
