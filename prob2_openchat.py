# coding=utf-8
class Statement(object):
    STYPE_ENTER = "Enter"
    STYPE_CHANGE = "Change"
    STYPE_LEAVE = "Leave"

    def __init__(self, stype, uid, nickname):
        super(Statement, self).__init__()
        self.stype = stype
        self.uid = uid
        self.nickname = nickname


def get_final_nickname_dict(structured_arr):
    ret = {}

    for each in structured_arr:
        if each.stype != Statement.STYPE_LEAVE:
            ret[each.uid] = each.nickname

    return ret


def get_structered(record):
    stype = ""
    uid = ""
    nickname = ""

    splited_record = record.split(' ')

    uid = splited_record[1]

    if splited_record[0] == "Enter":
        stype = Statement.STYPE_ENTER
    elif splited_record[0] == "Change":
        stype = Statement.STYPE_CHANGE
    elif splited_record[0] == "Leave":
        stype = Statement.STYPE_LEAVE
    else:
        assert False

    if stype != Statement.STYPE_LEAVE:
        nickname = splited_record[2]

    return Statement(stype, uid, nickname)


def get_structered_arr(record_arr):
    return [get_structered(each) for each in record_arr]


def get_chat_array(record_arr):
    chat_arr = []

    structured_arr = get_structered_arr(record_arr)
    nickname_dict = get_final_nickname_dict(structured_arr)

    for each in structured_arr:
        chat = ""
        if each.stype == Statement.STYPE_ENTER:
            chat = "{}님이 들어왔습니다.".format(nickname_dict[each.uid])
        if each.stype == Statement.STYPE_LEAVE:
            chat = "{}님이 나갔습니다.".format(nickname_dict[each.uid])

        if chat:
            chat_arr.append(chat)

    return chat_arr


if __name__ == '__main__':
    print(get_chat_array([
        "Enter uid1234 Muzi",
        "Enter uid4567 Prodo",
        "Leave uid1234",
        "Enter uid1234 Prodo",
        "Change uid4567 Ryan"
    ]))
