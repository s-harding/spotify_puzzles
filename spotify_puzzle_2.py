
#placeholder - file input to go here
album1 = [[30,'one'],[30,'two'],[15,'three'],[25,'four']]

def zipfs_law(album, top_n):
  q = album
  for i in range(len(album)):
    q[i][0] = (album[i][0]/(i+1))
  sorted(q, key = lambda l:l[1], reverse=True)
  print(q[:top_n])
  return q[:top_n]
  
  
zipfs_law(album1, 2)
