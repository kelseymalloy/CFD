import numpy as np

def gauss(X,Y,nx,ny,amp,radius):
    # returns gaussian bubble
    return amp*(np.exp(-((X-nx/2)**2/(2*(radius)**2) + (Y-ny/2)**2/(2*(radius)**2))))

def BC(u,v,wtype):
    if wtype == 0: # no slip boundary
        u[:, -2:] = 0
        #u[:, :2] = 0

        #v[:2,:] = 0
        v[-2:,:] = 0

    if wtype == 1: # periodicity
        u[:, -2:] = u[:,1]
        v[-2:,:] = v[:,1]       

        #v[0,:] = 0
        #v[-1,:] = 0


