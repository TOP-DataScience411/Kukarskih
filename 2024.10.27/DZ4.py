number = int(input("Enter your number, doesnt be more 999 and dont lower 100 "))

a1 = number // 100
a2 = (number // 10) % 10
a3 = number % 10

resultSumm = a1 + a2 + a3
resultMulti = a1 * a2 * a3
print ("your result are ", "summ ", resultSumm, "multi ", resultMulti)
