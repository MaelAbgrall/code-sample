"""convert a number to a big ascii caracter"""

# \n is 1 caracter
def convert(number):
    position = 0
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    line5 = ""
    line6 = ""
    line7 = ""
    asciiString = str(number)
    if (len(asciiString) > 10):
      return asciiString
    for caracters in asciiString:
      if(caracters == "0"):
        line1 = line1 + """   ###   """
        line2 = line2 + """  #   #  """
        line3 = line3 + """ #     # """
        line4 = line4 + """ #     # """
        line5 = line5 + """ #     # """
        line6 = line6 + """  #   #  """
        line7 = line7 + """   ###   """
      
      elif(caracters == "1"):
        line1 = line1 + """    #   """ 
        line2 = line2 + """  # #   """
        line3 = line3 + """    #   """
        line4 = line4 + """    #   """
        line5 = line5 + """    #   """
        line6 = line6 + """    #   """
        line7 = line7 + """  ##### """ 
              
      elif(caracters == "2"):
        line1 = line1 + """  #####  """
        line2 = line2 + """ #     # """
        line3 = line3 + """       # """
        line4 = line4 + """  #####  """
        line5 = line5 + """ #       """
        line6 = line6 + """ #       """
        line7 = line7 + """ ####### """
         
      elif(caracters == "3"):
        line1 = line1 + """  #####  """
        line2 = line2 + """ #     # """
        line3 = line3 + """       # """
        line4 = line4 + """  #####  """
        line5 = line5 + """       # """
        line6 = line6 + """ #     # """
        line7 = line7 + """  #####  """

      elif(caracters == "4"):
        line1 = line1 + """ #    #  """
        line2 = line2 + """ #    #  """
        line3 = line3 + """ #    #  """
        line4 = line4 + """ #    #  """
        line5 = line5 + """ ####### """
        line6 = line6 + """      #  """
        line7 = line7 + """      #  """

      elif(caracters == "5"):
        line1 = line1 + """ ####### """
        line2 = line2 + """ #       """
        line3 = line3 + """ #       """
        line4 = line4 + """ ######  """
        line5 = line5 + """       # """
        line6 = line6 + """ #     # """
        line7 = line7 + """  #####  """
         
      elif(caracters == "6"):
        line1 = line1 + """  #####  """
        line2 = line2 + """ #     # """
        line3 = line3 + """ #       """
        line4 = line4 + """ ######  """
        line5 = line5 + """ #     # """
        line6 = line6 + """ #     # """
        line7 = line7 + """  #####  """
         
      elif(caracters == "7"):
        line1 = line1 + """  #####  """
        line2 = line2 + """ #    #  """
        line3 = line3 + """     #   """
        line4 = line4 + """    #    """
        line5 = line5 + """   #     """
        line6 = line6 + """   #     """
        line7 = line7 + """   #     """
      
      elif(caracters == "8"):
        line1 = line1 + """  #####  """
        line2 = line2 + """ #     # """
        line3 = line3 + """ #     # """
        line4 = line4 + """  #####  """
        line5 = line5 + """ #     # """
        line6 = line6 + """ #     # """
        line7 = line7 + """  #####  """
      
      elif(caracters == "9"):
        line1 = line1 + """  #####  """
        line2 = line2 + """ #     # """
        line3 = line3 + """ #     # """
        line4 = line4 + """  ###### """
        line5 = line5 + """       # """
        line6 = line6 + """       # """
        line7 = line7 + """  #####  """

      elif(caracters == "."):
        line1 = line1 + """   """
        line2 = line2 + """   """
        line3 = line3 + """   """
        line4 = line4 + """   """
        line5 = line5 + """   """
        line6 = line6 + """   """
        line7 = line7 + """ # """
    
    concatenate = "\n" + line1 + "\n" + line2 + "\n" + line3 + "\n" + line4 + "\n" + line5 + "\n" + line6 + "\n" + line7 + "\n"
    return concatenate