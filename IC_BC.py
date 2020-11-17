import numpy as np

def gauss(X,Y,nx,ny,amp,radius):
    # returns gaussian bubble
    return amp*(np.exp(-((X-nx/2)**2/(2*(radius)**2) + (Y-ny/2)**2/(2*(radius)**2))))


def wave(X,Y,alpha,m,n,a,b):
   return alpha*(np.cos(m*np.pi*X/a))*(np.cos(n*np.pi*Y/b))

def wave_channel(X,Y,alpha,l):
   return alpha*(np.exp(-(X**2/l**2)))

def RossbyIC(p,u,v,X,Y,B):
   phi = 0.771*B**2*(1/(np.cosh((B*X)**2)))
   dphi_dx = -2*B*(np.tanh(B*X*phi))
   p[:,:] = ((6*Y**2 + 3)/4) * phi * (np.exp(-(Y**2/2)))
   u[:,:-1] = ((6*Y**2 - 9)/4) * phi * (np.exp(-(Y**2/2)))
   v[:-1,:] = 2*Y*dphi_dx*(np.exp(-(Y**2/2)))

   return p,u,v

def BC(u,v):
    u[:, 0] = 0.
    u[:, -1] = 0.

    v[0,:] = 0.
    v[-1,:] = 0.



