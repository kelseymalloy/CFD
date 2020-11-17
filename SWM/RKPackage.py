import numpy as np
from SWE_RHS import SWE_RHS

def RK3Step(p,u,v,f,depth,g,dx,dy,dt):
    # stage 1
    # compute the tendency terms
    rp, ru ,rv = SWE_RHS(p,u,v,f,depth,g,dx,dy)
    pt = p + dt*rp
    ut = u + dt*ru
    vt = v + dt*rv
   
    # stage 2
    rp, ru, rv = SWE_RHS(pt,ut,vt,f,depth,g,dx,dy)
    pt = 0.75 * p + 0.25 * (pt + dt*rp)
    ut = 0.75 * u + 0.25 * (ut + dt*ru)
    vt = 0.75 * v + 0.25 * (vt + dt*rv)

    # stage 3
    a = 1./3.
    b = 1.-a
    rp, ru, rv = SWE_RHS(pt,ut,vt,f,depth,g,dx,dy)
    p = a * p + b * (pt + dt*rp)
    u = a * u + b * (ut + dt*ru)
    v = a * v + b * (vt + dt*rv)
   
    return p,u,v

