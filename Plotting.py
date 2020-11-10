import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def UpdatePlots(it,p,u,v,XP,YP,XU,YU,XV,YV):
    #cmap = 'Reds'
    cmap= 'seismic'
    
    fig = plt.figure(figsize=[10,20])
    st = fig.suptitle('Shallow Water Model\nt = '+str(it), fontsize=22)

    ax1 = fig.add_subplot(311)
    cs=ax1.contourf(XP,YP,p,np.linspace(-1,1,40),cmap=cmap,extend='both')
    ax1.set_title('Eta',fontsize=18)
    ax1.set_xticks([])

    ax2 = fig.add_subplot(312)
    cs2=ax2.contourf(XU,YU,u,np.linspace(-1,1,40),cmap=cmap,extend='both')
    ax2.set_title('U',fontsize=18)
    ax2.set_xticks([])

    ax3 = fig.add_subplot(313)
    cs3=ax3.contourf(XV,YV,v,np.linspace(-1,1,40),cmap=cmap,extend='both')
    ax3.set_title('V',fontsize=18)

    plt.subplots_adjust(top=0.88,wspace=0.05, hspace=0.1)
    st.set_y(0.95)

    plt.show()
