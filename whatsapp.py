import pywhatkit

def send_message_inst():
    mobile = input('Phone number')
    message = input('Message')

    pywhatkit.sendwhatmsg_instantly(phone_no=mobile, message=message)

def main():
    send_message_inst()

if __name__ == '__main__':
    main()


