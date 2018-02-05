
album1 = [[30,'one'],[30,'two'],[15,'three'],[25,'four']]

def zipfs_law(album):
  q = []
  for i in range(len(album)):
    q.append(album[i][0]/(i+1))
  print(q)
  return q
  
  
zipfs_law(album1)
