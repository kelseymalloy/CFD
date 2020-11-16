import numpy as np

def gauss(X,Y,nx,ny,amp,radius):
    # returns gaussian bubble
    return amp*(np.exp(-((X-nx/2)**2/(2*(radius)**2) + (Y-ny/2)**2/(2*(radius)**2))))


def wave(X,Y,alpha,m,n,a,b):
   return alpha*(np.cos(m*np.pi*X/a))*(np.cos(n*np.pi*Y/b))


def BC(u,v):
    #if wtype == 0: # no slip boundary
    u[:, 0] = 0
    u[:, -1] = 0

    v[0,:] = 0
    v[-1,:] = 0

    #if wtype == 1: # periodicity
    #    u[:, -2:] = u[:,1]
    #    v[-2:,:] = v[:,1]       

        #v[0,:] = 0
        #v[-1,:] = 0


