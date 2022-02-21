from lib.tcprint import tcp, terr, tdecode, tlog
# from db.DataBase import DataBase
var1 = 'строка'  # вне контекста функции

# tcp.help()  # вызывает help-диалог


var0 = var1 = 0

def test():

  var2 = 'string val'  # вне контекста try, и var1=var2
  var3 = {'tcp_string': '<bg_red><red>red text on red background (NO) >'}

  tlog(var0=var0, var1=var1, var2=var2, var3=var3)


if __name__ == '__main__':
    test()
