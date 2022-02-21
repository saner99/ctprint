import sys  # for ctprint.err()
import traceback  # for ctprint.err()
# colorama - makes ANSI escape character sequences (for producing colored terminal text and cursor positioning) work under MS Windows.
from colorama import init, Fore, Back
from .help_message import h_m  # экземпляр класса со стрингами
# colorama autoreset=True - automatically back to default color
init(autoreset=True)

# from ctprint import ctp, ctdecode, cterr, ctlog # ctprint imports


tags: dict[str, dict[str, str]] = {

    'simple_styles': {'<plain>': Fore.WHITE + Back.BLACK,  # white text on black background
                      '<bw>': Fore.BLACK + Back.WHITE,  # black text on white background
                      '/>': Fore.RESET + Back.RESET,
                      '<info>': f'\n{Fore.YELLOW}{Back.BLACK}>>>>>>[Info]>>>>  ',
                      '<err>': f'\n{Fore.RED}{Back.BLACK}>>>>>>[Error]>>>>  ',
                      '<bw_info>': f'\n{Fore.BLACK}{Back.WHITE}>>>>>>[Info]>>>>  ',
                      '<bw_err>': f'\n{Fore.BLACK}{Back.WHITE}>>>>>>[Error]>>>>  '},

    'fore': {'<magenta>': Fore.MAGENTA, '<red>': Fore.RED, '<green>': Fore.GREEN,
             '<yellow>': Fore.YELLOW, '<blue>': Fore.BLUE, '<cyan>': Fore.CYAN,
             '<white>': Fore.WHITE, '<black>': Fore.BLACK, '<reset>': Fore.RESET},

    'back': {'<bg_magenta>': Back.MAGENTA, '<bg_red>': Back.RED, '<bg_green>': Back.GREEN,
             '<bg_yellow>': Back.YELLOW, '<bg_blue>': Back.BLUE, '<bg_cyan>': Back.CYAN,
             '<bg_white>': Back.WHITE, '<bg_black>': Back.BLACK, '<bg_reset>': Back.RESET}
}


class ctprint():

    def __init__(self, *strings: str) -> None:
        self.tags = tags

        if strings:
            print(self.decode(*strings))

    def decode(self, *strings: str) -> str:  # *args for ctprint.decode(string1, string2, string3)

        result_string = ''
        for string in strings:
            for tags_dict in self.tags:
                for tag in self.tags[tags_dict]:
                    string = string.replace(
                        tag, self.tags[tags_dict][tag])

            result_string += string  # натягивает стринги друг на друга
        return result_string

    def err(self, exception=None, comment: any = '') -> None:
        if comment:
            comment = f" comment: {str(comment)} "
        exc_type, exc_value, exc_traceback = sys.exc_info()
        # берёт тб последней ошибки. хорошо бы добавить проверку по exception
        ex_tb = traceback.extract_tb(exc_traceback, limit=1)[0]

        print(self.decode(  # the exception is not decoded so that the tags are visible in it
            f"\n<bw>>>>>>>[Error]>>>> in: {ex_tb.name}    line: {ex_tb.lineno} -> />   <red>{ex_tb.line}   <bw>>{comment}<plain><white>"), str(exception), self.decode(f"\n<bg_white><black>[file]>> <plain>   {ex_tb.filename}"))

    def log(self, **vars) -> None:

        for varname, varvalue in vars.items():
            print(self.decode(f'<bw> {str(varname)} \t:'), str(varvalue))

    def help() -> None:
        help_msg = h_m.help_info + h_m.description + h_m.tags + h_m.methods
        print(ctprint().decode(help_msg).replace(
            'PRE', ''))  # PRE - separates the tags

        if input(ctdecode("""
    <magenta>Press <bw> Y /><magenta> if u wanna see short live example: />""")).lower() == 'y':

            print(ctprint().decode(h_m.test_example).replace('PRE', ''))
            ctprint("<info> def test() output:/>\n")
            test()

        ctprint(h_m.ending)


# for imports
ctp = ctprint
cterr = ctp().err
ctdecode = ctp().decode
ctlog = ctp().log

# example:
# ./test.py
# from ctprint import ctp, cterr, ctdecode

# ctp.help()  # print help message


def test():  # usage example

    try:

        ctp('<bw> b&w !!! /><magenta> magenta <plain> plain <green>green />etc')
        1/0  # for error's view example

    except Exception as _ex:

        # cterr(Exception, your_comment)
        cterr(_ex, [{'excepted': 3.1415926535}])
