def is_pallindrome(string):
  left = 0
  right = len(string) - 1
  if left >= right:
    return True
  if string[left] == string[right]:
    return is_pallindrome(string[1:-1])
  return False