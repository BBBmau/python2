# Mauricio Alvarez Leon
class Message:
    def __init__(email,_addressSender,_addressRecipient, _msgText):
        email.addressSender = addressSender
        email.addressRecipient= addressRecipient
        email.msgText = ""
    
    def add_line(message:str):
        email.msgText += message + "\n"
    
    def show()-> str:
        fullMessage = "TO: " + email.addressRecipient + "\n"
        fullMessage += "FROM: " + email.addressSender + "\n"
        
        fullMessage += "\n" + email.msgText
        
        return fullMessage

    def write(fileName: str):
        msg = open(fileName, 'w')
        msg.write(show())
        msg.close()
        
    def __str__()-> str:
        msgSummary = "TO: " + email.addressRecipient + " FROM: " + email.addressSender + " : "
        for i in 25:
            msgSummary += email.msgText[i]
        
        return msgSummary
    
    def get_sender():
        return email.addressSender
    
    def get_recipient():
        return email.addressRecipient
        
class Mailbox(message):
    def __init__(eMsg, __ownerAddress, **__inMsg: message, **__outMsg: message):
        eMsg.ownerAddress = ownerAddress
    
    def add_message(msg: message):
        if(msg.addressSender == ownerAddress):
            outMsg.append(msg)
        
        if(msg.addressRecipient == ownerAddress):
            inMsg.append(msg)
    
    def display():
        print("INBOX:")
        for i in len(inMsg):
            print(i + ". TO: " + ownerAddress + " FROM " + outMsg[i].get_tecipient())
        
        print("\nOUTBOX:")
        for i in len(outMsg):
            print((i+1) + ". TO: " + ownerAddress + " FROM " + inMsg[i].get_sender())
    
    def get_message(index: int, ):
        pass

// MISSING DELETE AND FILTER METHODS
    
    def __str__():
        print(ownerAddress + "'s Mailbox - " + "contains " + str(len(inMsg) + len(outMsg)) + " messages")
        
