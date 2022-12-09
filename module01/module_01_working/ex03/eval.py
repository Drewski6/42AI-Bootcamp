class Evaluator:
    """
    Takes 2 lists. First is a list of words. Second a list of coeficients.\n
    zip and enumerate will find the strlen of each word and multiply it by the coef\n
    """
    def __init__(self):
        pass

    def zip_evaluate(self, words_lst, coefs_lst):
        """
        Uses zip function to find of sum (strlen * coef)
        """
        assert (isinstance(words_lst, list)), "Words should be a list of strings."
        for item in words_lst:
            assert (isinstance(item, str)), "Words should be a list of strings"
        assert (isinstance(coefs_lst, list)), "coefs should be a list of floats"
        for item in coefs_lst:
            assert (isinstance(item, float)), "coefs should be a list of strings"
        if len(words_lst) != len(coefs_lst):
            return -1
        result = 0
        for item in zip(words_lst, coefs_lst):
            result += int(len(item[0]) * item[1])
        return result
        

    def enumerate_evaluate(self, words_lst, coefs_lst):
        """
        Uses enumerate function to find of sum (strlen * coef)
        """
        assert (isinstance(words_lst, list)), "Words should be a list of strings."
        for item in words_lst:
            assert (isinstance(item, str)), "Words should be a list of strings"
        assert (isinstance(coefs_lst, list)), "coefs should be a list of floats"
        for item in coefs_lst:
            assert (isinstance(item, float)), "coefs should be a list of strings"
        if len(words_lst) != len(coefs_lst):
            return -1
        result = 0
        for item, word in enumerate(words_lst):
            result += int(len(word) * coefs_lst[item])
        return result

# Testing

# Evaluator = Evaluator()

# words = ["Le", "Lorem", "Ipsum", "est", "simple"]
# coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
# print(Evaluator.zip_evaluate(words, coefs))

# words = ["Le", "Lorem", "Ipsum", "est", "simple"]
# coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
# print(Evaluator.enumerate_evaluate(words, coefs))

# words = ["Le", "Lorem", "Ipsum", "n", "est", "pas", "simple"]
# coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
# print(Evaluator.zip_evaluate(words, coefs))

# words = ["Le", "Lorem", "Ipsum", "n", "est", "pas", "simple"]
# coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
# print(Evaluator.enumerate_evaluate(words, coefs))
