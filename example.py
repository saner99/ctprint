from tcprint import tcp, terr, tdecode, tlog
# from db.DataBase import DataBase
var1 = 'строка'  # вне контекста функции

# tcp.help()  # вызывает help-диалог


def test():
    # db = DataBase()
    # db.connect()

    # # # db.execute("""CREATE DATABASE email_inbot""")
    # # # db.execute("""""")

    # db.close_connection()
    var2 = 'строка'  # вне контекста try, и var1=var2
    err0 = tdecode('<err>вполне ожидаемая ошибка при делении на 0/>')
    try:
        var3 = {'tagged': '<bg_red><black>output/>'}
        tcp('<bw>\n\\ttext\t<bg_green>text/>\tdefault text')

        tlog(var1=var1, var2=var2, var3=var3)

        1/0
    except Exception as _ex:
        terr(_ex)

        print(err0)


if __name__ == '__main__':
    test()
