import numpy as np

def avg_x(data):
    return 0.5*(data[:,:-1] + data[:,1:])

def avg_y(data):
    return 0.5*(data[:-1,:] + data[1:,:])

def d_dx(data,dx):
    return (data[:,1:] - data[:,:-1]) / dx

def d_dy(data,dy):
    return (data[1:,:] - data[:-1,:]) / dy

def calc_budget(p,u,v,h,f,g,dx,dy):
    energy = 0.5*h*(avg_x(u**2) + avg_y(v**2)) + (0.5*g*p**2)

    dv_dx = d_dx(v,dx)
    du_dy = d_dy(u,dy)

    q = np.zeros((p.shape[0]+1,p.shape[1]+1))
    q[1:-1,1:-1] = (dv_dx[1:-1,:] - du_dy[:,1:-1] + f[1:-1,1:-1])/(avg_x(avg_y(h)))
    
    enstrophy = (avg_x(avg_y(h)))*q[1:-1,1:-1]**2
    
    V = dx*dy*np.sum(p)

    return energy,enstrophy,V



