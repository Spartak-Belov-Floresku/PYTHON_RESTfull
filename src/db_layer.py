import json

class ProcessData():
    def __init__(self, responce):
        self.__responce = responce
        self.__CreateJSON()

    def __CreateJSON(self):
        try:
            json_obj = json.loads(self.__responce.read().decode("utf-8"))
            with open("file.json", "w") as file_json:
                json.dump(json_obj, file_json)
                print("File: ",file_json.name," has been created")
        except Exception as e:
            err = str(e)
            print("Data base layer error :",err)
