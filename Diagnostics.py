import numpy as np

def calc_budget(p,u,v,h,f):
   energy = 0.5*h*(avgx(u**2) + avgy(v**2)) + 0.5*g*p^2
   q = (d_dx(v) - d_dy(u) + f)/(avgx(avgy(h)))
   enstrophy = (avgx(avgy(h)))*q**2

   return energy,q,enstrophy
