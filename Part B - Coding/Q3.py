def permute(s):
  result = []
  chars =list(s)

  def backtrack(index):
    if index == len(chars):
      result.append("".join(chars))
      return

    for i in range(index, len(chars)):
      chars[index], chars[i] = chars[i], chars[index]
      backtrack(index + 1)
      chars[index], chars[i] = chars[i], chars[index]

  backtrack(0)
  return result

print(permute("abc"))
print(permute("ab"))