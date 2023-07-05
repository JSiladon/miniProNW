class chatDB():
    def __init__(self):
        self.database = {}
        self.msg_id = 0

    def InsertMessage(self, msg):
        self.msg_id += 1
        self.database[self.msg_id] = msg
    def InsertUsername(self, msg):
        self.msg_id += 1
        self.database[self.msg_id] = msg

    def InsertPwd(self, msg):
        self.msg_id += 1
        self.database[self.msg_id] = msg
                    
    def getMessage(self, msgID):
        if len(self.database) == 0:
            return "No message yet!"
        elif msgID == 0:
            tmp = ""
            for key, data in self.database.items():
                tmp = tmp + data + "\n"
            return tmp
        elif msg != 0:
            tmp = self.database[msg]
            return tmp
        else:
            return "\n"


    def getlogin(self, msgID):
        if len(self.database) == 0:
            return "No UserName yet!"
        elif msgID == 0:
            tmp = ""
            for key, data in self.database.items():
                tmp = tmp + data + "\n"
            return tmp
        elif msgID != 0:
            tmp = self.database[msgID]
            return tmp
        else:
            return "\n"


