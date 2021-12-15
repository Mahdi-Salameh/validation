def predicate_model_checker(function, value):
    retval = function(value)
    if not isinstance(retval, bool):
        print("function did not return a bool")
        return None
    if retval:
        print("True")
    else:
        print("False")


# predicate_model_checker(sum, [1, 2, 3])
# predicate_model_checker(lambda x: True, [1, 2, 3])
