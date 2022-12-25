tuples=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
sorted_list = []
for t in tuples:
  for i, t2 in enumerate(sorted_list):
    if t[1] < t2[1]:
      sorted_list.insert(i, t)
      break
  else:
    sorted_list.append(t)
print(sorted_list)

      