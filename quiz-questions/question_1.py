def question_1():
    """Return the correct value for the following question.

    **IMPORTANT!** Return the actual value of `c`, not just the answer option.

    Take a look at the following code and answer:
    # === CODE STARTS === #
    a = 10
    b = 3
    c = 7


    def test_scope(b):
        a = 11
        return a + b + c

    c = c + test_scope(5)
    # === CODE ENDS === #

    What will be the final value of the variable c?
    """
    # Return the CORRECT value of `c`
    pass
#test_scope(5) returns a=11 + b=5 + c=7 === 23

#c return c=7 + test_scope(5)=23 === 30 Final answer
