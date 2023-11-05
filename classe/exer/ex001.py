def MinWindowSubstring(strArr):
  list = []
  list2 = []
  list3 = []
  list4 = []
  list5 = []
  dic = {}
  for e in strArr[1]:
    list.append(e)
    dic[f'{e}'] = strArr[1].count(e)

  for c in strArr[1]:
    p = strArr[0].index(c)
    list2.append(strArr[0][p:-1])

  #print(strArr[1])
  #print(dic)
  #print(list2)
  #c = ''

  for el in list2:
    while list.count(el[-1]) == 0:
      el = el[:-1]
      #el = el.replace(el[-1], '')"""
    list3.append(el)
  #print(list3)


  for ele in list3:
    if len(ele) > 5:
      list4.append(ele)
  #print(list4)

  for elem in list4:
    for c in elem:
      if elem[-1] in list:
        if elem.count(elem[-1]) != dic[elem[-1]]:
          #print(elem.count(elem[-1]))
          #print(dic[elem[-1]])
          elem = elem[:-1]
      else:
        elem = elem[:-1]
      if elem[0] in list:
        if elem.count(elem[0]) != dic[elem[0]]:
          elem = elem[1:]
      else:
        elem = elem[1:]

    list5.append(elem)
    #print(elem)
  #print(list5)
  # code goes here
  return list5[0]


# keep this function call here
array = ["ahffaksfajeeubsne", "jefaa"]

print(MinWindowSubstring(array))