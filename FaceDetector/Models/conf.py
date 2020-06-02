import json

class ConfigurationFile:
    
    def __init__(self, frontalFace):
        self.frontalFace = frontalFace

    @staticmethod    
    def get():
        try:
            # read file
            with open('conf.json', 'r') as myfile:
                data = myfile.read()

            # parse file
            obj = json.loads(data)
            conf_dict = json.loads(data)
            conf_object = ConfigurationFile(**conf_dict)
            return conf_object
        except:
            raise Exception('It was not possible to read conf file.')