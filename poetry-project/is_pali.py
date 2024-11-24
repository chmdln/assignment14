def is_pali(s):
    '''
        Checks if the given string is a palindrome, ignoring case and non-alphanumeric characters.

        Parameters:
            s (str): The input string to check.

        Returns:
            bool: True if the input is a palindrome.

        Raises:
            TypeError: If the input is not a string.
    '''
    
    if not isinstance(s, str):
        raise TypeError("Input must be a string.")

    valid = set('abcdefghijklmnopqrstuvwxyz0123456789')
    s = "".join(char.lower() for char in s if char.lower() in valid)
        
    l, r = 0, len(s)-1
    if not s: 
        return True 

    while l < r: 
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True 
        