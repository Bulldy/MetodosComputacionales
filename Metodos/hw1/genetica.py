import random
import math
import matplotlib.pyplot as plt
import numpy as np

class Expresion:
    def __init__(self,kr=1.0, kp=60.0, yr=0.2, yp=(1.0/30.0),r0=0.0, p0=0.0, dt=0.0003,Tf=150.0):
        self.kr=kr
        self.kp=kp
        self.yr=yr
        self.yp=yp
        self.r=np.arange(0,Tf+dt,dt)
        self.p=np.arange(0,Tf+dt,dt)
        self.t=np.arange(0,Tf+dt,dt)
        self.dt=dt
        self.Tf=Tf
        self.r[0]=r0
        self.p[0]=p0

    def resuelve(self):
        for i in range(len(self.t)):
            pcarn=self.kr*self.dt
            pdarn=self.yr*self.r[i]*self.dt
            pcp=self.kp*self.r[i]*self.dt
            pdp=self.yp*self.p[i]*self.dt
            rand_carn=random.random()
            rand_darn=random.random()
            rand_cp=random.random()
            rand_dp=random.random()
            
            
    def grafica(self,analitica=False):
        if(analitica==False):
            fig=plt.figure()
            plt.plot(self.t,self.r)
            ax=plt.axes()
            ax.set_xlabel("Tiempo (min)")
            ax.set_ylabel("Numero de ARNm")
            file='r_t'
            plt.savefig(file+'.pdf',format='pdf')
            plt.close()
            
            fig2=plt.figure()
            plt.plot(self.t,self.p)
            ax2=plt.axes()
            ax2.set_xlabel("Tiempo (min)")
            ax2.set_ylabel("Numero de proteinas")
            file2='p_t'
            plt.savefig(file2+'.pdf',format='pdf')
            plt.close()

        else:
            anr=(self.kr/self.yr)*(1-np.exp(-1*self.yr*self.t))
            anp=((self.kr*self.kp)/(self.yr*self.yp))*(1-(np.exp(-self.yp*self.t))+(self.yp/(self.yp+self.yr))*((np.exp(-self.yp*self.t))-(np.exp(-self.yr*self.t))))
            fig=plt.figure()
            plt.scatter(self.t,self.r)
            plt.plot(self.t,anr)
            ax=plt.axes()
            ax.set_xlabel("Tiempo (min)")
            ax.set_ylabel("Numero de ARNm")
            file='r_t'
            plt.savefig(file+'.pdf',format='pdf')
            plt.close()

            fig2=plt.figure()
            plt.scatter(self.t,self.p)
            plt.plot(self.t,anp)
            ax2=plt.axes()
            ax2.set_xlabel("Tiempo (min)")
            ax2.set_ylabel("Numero de proteinas")
            file2='p_t'
            plt.savefig(file2+'.pdf',format='pdf')
            plt.close()