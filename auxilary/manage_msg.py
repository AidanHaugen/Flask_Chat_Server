def get_msg_hist():
    f = open('./files/msg_hist.txt', 'r')

    msg_hist = f.readlines()

    f.close()

    return msg_hist

def send_msg(msg):
    if msg == '':
        return

    f = open('./files/msg_hist.txt', 'a')

    f.write(f'{msg}\n')

    return
