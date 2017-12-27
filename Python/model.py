"""this is where we store our data:
the menu string,
the warning string
the result & the ascii result
"""
class Model:

  def __init__(self):
    self.menuString = """\

:::'##:::::'##:'########:'##::::::::'######:::'#######::'##::::'##:'########::::'####::::
::: ##:'##: ##: ##.....:: ##:::::::'##... ##:'##.... ##: ###::'###: ##.....::::: ####::::
::: ##: ##: ##: ##::::::: ##::::::: ##:::..:: ##:::: ##: ####'####: ##:::::::::: ####::::
::: ##: ##: ##: ######::: ##::::::: ##::::::: ##:::: ##: ## ### ##: ######::::::: ##:::::
::: ##: ##: ##: ##...:::: ##::::::: ##::::::: ##:::: ##: ##. #: ##: ##...::::::::..::::::
::: ##: ##: ##: ##::::::: ##::::::: ##::: ##: ##:::: ##: ##:.:: ##: ##::::::::::'####::::
:::. ###. ###:: ########: ########:. ######::. #######:: ##:::: ##: ########:::: ####::::
::::...::...:::........::........:::......::::.......:::..:::::..::........:::::....:::::
                    ______________________________________________
                    Type "help" & press ENTER for more information

    """

    self.warningString = """\
    Help:
        +       Addition
        -       Substraction
        *       Multiply
        /       Divide
        rt      n Root
        x       Power
        clear   clear result
        help    this menu    
        exit    exit

    1. Press the desired operation & press ENTER
    2. Type a integer or a float number & press ENTER
    3. Result is shown with big ascii caracters
    4. Repeat or type exit

    """
    self.result = 0.0
    self.asciiresult = """\
   #####
  ##   ##
 ##     ##
 ##     ##
 ##     ##
  ##   ##
   #####

    """
    return

  #Python don't have encapsulation, instead, we use properties


  #menu string
  @property
  def menuString(self):
    return self.__menuString

  @menuString.setter
  def menuString(self, menuString):
    self.__menuString = menuString



  #help / warning string
  @property
  def warningString(self):
    return self.__warningString

  @warningString.setter
  def warningString(self, warningString):
    self.__warningString = warningString




  #RESULT
  @property
  def result(self):
    return self.__result

  @result.setter
  def result(self, result):
    self.__result = result




  #ASCIIRESULT
  @property
  def asciiresult(self):
    return self.__asciiresult

  @asciiresult.setter
  def asciiresult(self, asciiresult):
    self.__asciiresult = asciiresult
