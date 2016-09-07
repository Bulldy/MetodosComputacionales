import random
import math
import matplotlib.pyplot as plt
import numpy as np

class Expresion:
    def __init__(self,kr=1.0, kp=60.0, yr=0.2, yp=(1.0/30.0),r0=0.0, p0=0.0, dt=0.0003,Tf=150.0):
        self.kr=kr*1.0
        self.kp=kp*1.0
        self.yr=yr*1.0
        self.yp=yp*1.0
        self.r=np.arange(0,(Tf+dt)*1.0,dt*1.0)
        self.p=np.arange(0,(Tf+dt)*1.0,dt*1.0)
        self.t=np.arange(0,(Tf+dt)*1.0,dt*1.0)
        self.dt=dt*1.0
        self.Tf=Tf*1.0
        self.r[0]=r0*1.0
        self.p[0]=p0*1.0

    def resuelve(self):
        for i in range(0,len(self.t)-1):
            pcarn=self.kr*self.dt
            pdarn=self.yr*self.r[i]*self.dt
            pcp=self.kp*self.r[i]*self.dt
            pdp=self.yp*self.p[i]*self.dt
            rand_carn=random.random()
            rand_darn=random.random()
            rand_cp=random.random()
            rand_dp=random.random()
            cr=0
            cp=0
            if(rand_carn<pcarn):
                cr=cr+1
            if(rand_darn<pdarn):
                cr=cr-1
            if(rand_cp<pcp):
                cp=cp+1
            if(rand_dp<pdp):
                cp=cp-1
            if(self.r[i]==0 and cr<0):
                self.r[i+1]=0
            if(self.p[i]==0 and cp<0):
                self.p[i+1]=0
            if(self.r[i]!=0):
                self.r[i+1]=self.r[i]+cr
            if(self.p[i]!=0):
                self.p[i+1]=self.p[i]+cp

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
            plt.plot(self.t,self.r,label="Estocastica")
            plt.plot(self.t,anr,label="Analitica")
            ax=plt.axes()
            ax.set_xlabel("Tiempo (min)")
            ax.set_ylabel("Numero de ARNm")
            plt.legend(loc=2)
            file='r_t'
            plt.savefig(file+'.pdf',format='pdf')
            plt.close()

            fig2=plt.figure()
            plt.plot(self.t,self.p,label="Estocastica")
            plt.plot(self.t,anp,label="Analitica")
            ax2=plt.axes()
            ax2.set_xlabel("Tiempo (min)")
            ax2.set_ylabel("Numero de proteinas")
            plt.legend(loc=4)
            file2='p_t'
            plt.savefig(file2+'.pdf',format='pdf')
            plt.close()
