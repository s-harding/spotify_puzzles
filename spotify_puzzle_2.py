
import copy


#placeholder - file input to go here
album1 = [[30.,'one'],[30.,'two'],[15.,'three'],[25.,'four']]

def zipfs_law(album, top_n):
  q = copy.deepcopy(album)
  ans = []
  expt = []
  for i in range(len(album)):
    val = album[0][0]/float((i+1.))
    #print(val)
    expt.append(val)
    q[i][0] = album[i][0]/expt[i]
  q = sorted(q, key=lambda x: x[0], reverse=True)

  ans = [sublist[1:] for sublist in q[:top_n]]
  return ans
  
print(zipfs_law(album1, 2))
