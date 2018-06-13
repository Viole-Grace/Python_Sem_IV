def partition(ls):
  result=[]
  for name in ls:
    if name[0].lower() in 'abcdefghijklm':
      result.append(name)
  print(result)
word=input("Enter names please: ")
splitwords=word.split()
partition(splitwords)
