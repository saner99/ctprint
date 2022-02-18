# from tcprint import tcp, tdecode, terr, tlog


class help_message():

    help_info: str = f"""
<bw>>>>>>>[ tcprint.help() ]>>>> <plain><magenta> Help info: <plain>
<magenta>{'-'*40}/>"""

    description = f"""
- All tcprint opening tags are always enclosed in angle brackets: '<magenta>< ><plain>'
- tcprint have ONLY ONE CLOSING TAG - <magenta>/PRE>/> (reset all formating to sys default)
- for RESET FORMATING to default u can use tags <magenta><PREreset><plain> and <magenta><PREbg_reset><plain>.
Also u can format text to white and background to black using <magenta><PREplain><plain>
"""
    tags: str = f"""
    <magenta>{'-'*18}
    Simple-usage tags:
    {'-'*18}/>
    
        <bw><PREplain>/>\t: <plain>white text on black background/>
        <bw><PREbw>/>\t: <bw>black text on white background/>
        <bw>/PRE>/>\t: />your terminal's default formating/>
        
    <magenta>{'-'*22}
    Foregroung color tags:
    {'-'*22}/>
    
        <bw><PREmagenta><plain>\t: <magenta>magenta text/>
        <bw><PREred><plain>\t\t: <red>red text/>
        <bw><PREgreen><plain>\t\t: <green>green text/>
        <bw><PREyellow><plain>\t: <yellow>yellow text/>
        <bw><PREblue><plain>\t\t: <blue>blue text/>
        <bw><PREcyan><plain>\t\t: <cyan>cyan text/>
        <bw><PREwhite><plain>\t\t: <white>white text/>
        <bw><PREblack><plain>\t\t: <black>black text/> <- it's here:)
        <PREmagenta> text <bw><PREreset>/> text/>\t: <magenta> text <reset>text (result of reset tag)/>

    <magenta>{'-'*22}
    Background color tags:
    {'-'*22}/>
    
        <bw><PREbg_magenta>/>\t: <bg_magenta> magenta background/>
        <bw><PREbg_red>/>\t: <bg_red> red background/>
        <bw><PREbg_green>/>\t: <bg_green> green background/>
        <bw><PREbg_yellow>/>\t: <bg_yellow> yellow background/>
        <bw><PREbg_blue>/>\t: <bg_blue> blue background/>
        <bw><PREbg_cyan>/>\t: <bg_cyan> cyan background/>
        <bw><PREbg_white>/>\t: <bg_white> white background/>
        <bw><PREbg_black>/>\t: <bg_black> black background/>
        <PREbg_magenta> text <bw><PREbg_reset>/> text/>\t: <bg_magenta> text <bg_reset>text (result of background's reset tag)/>

    <magenta>{'-'*17}
    Tags for logging:
    {'-'*17}/>
    
        <bw><PREinfo>/>here any your info /PRE> and any text then/> :
        \t<info> here any your info /> and any text then

        <bw><PREerr>/>here any your text of exception /PRE> and any text then/> :
        \t<err> here any your text of exception /> and any text then

        <bw><PREbw_info>/>here any your info /PRE> and any text then/> :
        \t<bw_info> here any your b&w info /> and any text then

        <bw><PREbw_err>/>here any your b&w text of exception /PRE> and any text then/> :
        \t<bw_err> here any your text of exception /> and any text then
        """
    methods: str = f"""
    <magenta>{'-'*24}
    Logging tcprint methods:
    {'-'*24}/>
    <magenta>from<red> tcprint <magenta>import<red> tcp/>, <red>tdecode/>, <red>terr/>, <red>tlog/> # for example
        
        <blue>tcp/>(<green>'<PREbw>text\t\PRE>'/>)/> output:
        <bw>text\t/>
        
        <blue>tdecode/>(<green>'<PREbw>text\t\PRE>'/>)/> return-> <bw>text\t/>
        
        <blue>terr/>(<yellow>Exception/>, <green>'your comment'/>)/> error message output:
<bw>>>>>>>[Error]>>>> in: <name>    line: <line index> ->/><red>    <the line's code>   <bw>> comment: your comment /> <excaption>
<bw>[file]>> />   <path to file> 

        <red>var1/>=<yellow>0
        <red>var2/>=<green>'text'
        <red>var3/>="""+"""{<green>'dict_key','<PREbw>text/PRE>'/>}"""+"""
        <blue>tlog/>(<red>var1 = <red>var1/>, <red>var2/> = <red>var2/> , <red>var3/> = <red>var3/>)/> log message output:
 <bw>var1   :/> 0
 <bw>var2   :/> text
 <bw>var3_dict_key  :/> {'dict_key','<PREbw>text/PRE>'}
        """
    ending: str = """
    <magenta>It's all today ☺/> happy consolling!"""

    test_example: str = """
/>#./test.py
<magenta>from<red> tcprint <magenta>import<red> tcp/>, <red>tdecode/>, <red>terr/>, <red>tlog/>

# tcp.help()  # print help message

<magenta>def/> <blue>test/>():

    <magenta>try/>:
    
        <blue>tcp/>(<green>'<PREbw> b&w !!! /PRE><PREmagenta> magenta <PREplain> plain <PREgreen>green /PRE>etc'/>)
        <yellow>1<blue>/<yellow>0/>  # for error's view example
        
    <magenta>except<yellow> Exception<magenta> as <red>_ex/>:
        
        <blue>terr/>(<red>_ex/>, [{<green>'excepted'/>: <yellow>3.1415926535/>}]) # terr(Exception, your_comment)


<magenta>if <red>__name__ <blue>==<green> '__main__'/>:
    <blue>test/>()"""
