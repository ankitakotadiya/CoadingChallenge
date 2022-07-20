def multiply(num1, num2):

  sign = -1 if num1[0] < 0 or num2[0] < 0 else 1

  num1[0],num2[0] = abs(num1[0]),abs(num2[0])

  result = [0] * (len(num1) + len(num2))
  for i in range(len(num1)-1,-1,-1):

    for j in range(len(num2)-1,-1,-1):

      result[i+j+1] += num1[i]*num2[j]
      result[i+j] += result[i+j+1]//10
      result[i+j+1] %= 10

  l = 0
  r = len(result)

  while l < r:

    if result[l] != 0:
      break

    l+=1
  result = result[l:r]
  return [sign * result[0]] + result[1:]
