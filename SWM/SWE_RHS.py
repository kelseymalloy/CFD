import numpy as np
from Diagnostics import avg_x, avg_y, d_dx, d_dy

def SWE_RHS(p,u,v,f,depth,g,dx,dy):
    rp = np.zeros_like(p)
    ru = np.zeros_like(u)
    rv = np.zeros_like(v)
    
    # form the total depth h on p-points
    h = depth + p
    
    # compute x-average of h on u-points
    havg_x = np.zeros(ru.shape)
    havg_x[:,1:-1] = avg_x(h)
    havg_x[:,0] = h[:,0]
    havg_x[:,-1] = h[:,-1]
    
    # compute x-mass flux U=hbx*u on u-points
    U = havg_x * u

    # compute y-average of h on v-points, hby
    havg_y = np.zeros(rv.shape)
    havg_y[1:-1,:] = avg_y(h)
    havg_y[0,:] = h[0,:]
    havg_y[-1,:] = h[-1,:]
    
    # compute y-mass flux V=hby*v on v-points    
    V = havg_y * v
    
    # compute the x-gradient of (U)_x=gradx(U)
    dU_dx = d_dx(U,dx)
    
    # add-in the y-gradient of (V)_y=grady(V)
    dV_dy = d_dy(V,dy)

    rp = -dU_dx-dV_dy

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
    q = np.zeros((rp.shape[0]+1,rp.shape[1]+1))
    q[1:-1,1:-1] = (dv_dx[1:-1,:] - du_dy[:,1:-1] + f[1:-1,1:-1])/(avg_x(avg_y(h)))
    
    # compute avx(V) and avy(U) on z-points
    Vavg_x = np.zeros((rp.shape[0]+1,rp.shape[1]+1))
    Uavg_y = np.zeros((rp.shape[0]+1,rp.shape[1]+1))
   
    Vavg_x[:,1:-1] = avg_x(V)
    Vavg_x[:,0] = V[:,0]
    Vavg_x[:,-1] = V[:,-1]
    Uavg_y[1:-1,:] = avg_y(U)
    Uavg_y[0,:] = U[0,:]
    Uavg_y[-1,:] = U[-1,:]

    # compute avy(q*V) on u-points and add it to ru
    qVavg_y = np.zeros(ru.shape)
    qVavg_y = avg_y(q*Vavg_x)
    
    ru[:,:] = ru[:,:]+qVavg_y

    # compute avx(q*U) on v-points and add it to rv
    qUavg_x = np.zeros(rv.shape)    
    qUavg_x = avg_x(q*Uavg_y)
    rv[:,:] = rv[:,:]-qUavg_x
    
    return rp,ru,rv
