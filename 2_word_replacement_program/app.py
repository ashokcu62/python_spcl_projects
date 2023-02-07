def word_replacement_app():
    str=" hello guys hello hello hello"

    sn=f"""
    {str}
    ------------------------------------
    you can change the given sentence 
    """

    print(sn)
    word_to_replace=input("which word do you need to change :")
    new_word=input("enter the replacement word :")
    str=str.replace(word_to_replace,new_word)

    sn=f"""
    as i said the  word is replaced 
    -------------------------------------
    {str}
    """

    print(sn)


word_replacement_app()