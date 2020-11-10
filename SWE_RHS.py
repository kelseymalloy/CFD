import numpy as np
from Diagnostics import avg_x, avg_y, d_dx, d_dy

def SWE_RHS(p,u,v,f,depth,g,dx,dy):
    rp = np.zeros_like(p)
    ru = np.zeros_like(u)
    rv = np.zeros_like(v)
    
    # form the total depth h on p-points
    h = depth + p
    
    # compute x-average of h on u-points
    havg_x = avg_x(h)
    
    # compute x-mass flux U=hbx*u on u-points
    U = havg_x * u[:,1:-1]

    # compute y-average of h on v-points, hby
    havg_y = avg_y(h)
    
    # compute y-mass flux V=hby*v on v-points    
    V = havg_y * v[1:-1,:]
    
    # compute the x-gradient of (U)_x=gradx(U)
    dU_dx = d_dx(U,dx)
    
    # add-in the y-gradient of (V)_y=grady(V)
    dV_dy = d_dy(V,dy)

    rp[1:-1,1:-1] = -dU_dx[1:-1,:]-dV_dy[:,1:-1]

    # pressure is tp = g*p + 0.5* ( avx(u^2)+avy(v^2) )
    tp = g*p + 0.5*(avg_x(u**2)+avg_y(v**2))
    
    # x-gradient of tp and add it to ru
    dtp_dx = d_dx(tp,dx)  
    ru[:,1:-1] = -dtp_dx
    
    
    # y-gradient of tp and add it to rv
    dtp_dy = d_dy(tp,dy)
    rv[1:-1,:] = -dtp_dy
    
    # Coriolis term
    # compute q = (v_x - u_y + f)/avx(avy(h))
    dv_dx = d_dx(v,dx)
    du_dy = d_dy(u,dy)
    q = (dv_dx[1:-1,:] - du_dy[:,1:-1] + f[1:-1,1:-1])/(avg_x(avg_y(h)))
    
    # compute avx(V) and avy(U) on z-points
    Vavg_x = avg_x(V)
    Uavg_y = avg_y(U)
    
    # compute avy(q*V) on u-points and add it to ru
    qVavg_y = avg_y(q*Vavg_x)
    ru[1:-1,1:-1] = qVavg_y

    # compute avx(q*U) on v-points and add it to rv
    qUavg_x = avg_x(q*Uavg_y)
    rv[1:-1,1:-1] = -qUavg_x
    
    #print(rp.shape,ru.shape,rv.shape)

    return rp,ru,rv
