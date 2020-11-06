import numpy

def gauss(X,Y,nx,ny,amp,radius):
   return amp*(np.exp(-((X-nx/2)**2/(2*(radius)**2) + (Y-ny/2)**2/(2*(radius)**2))))

def InitialConditions(p,u,v):
   p = gauss(X,Y,nx,ny,5,5)
   u = np.zeros_like(u)
   v = np.zeros_like(v)



