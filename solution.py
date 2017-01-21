def answer(l, t):
  total = 0
  for first_index in range(len(l)):
    total = l[first_index]
    if total == t:
      return [first_index, first_index]
    for second_index in range(len(l) - (first_index+1)):
      total = total + l[first_index+second_index+1]
      if total == t:
        return [first_index,first_index+second_index+1]
  return [-1,-1]
