import random
class Walk:
    def __init__(self, n_points=10000, step=1.0, pos_init=0):
        self.n_points = n_points
        self.pos = range(n_points)
        self.time = range(n_points)
        self.step = step
        self.pos[0] = pos_init

    def run(self):
        for i in range(1,self.n_points):
            r = random.random()
            if(r<=0.5):
                step = self.step;
            else:
                step = -self.step

            self.pos[i] = self.pos[i-1] + step
            self.time[i] = self.time[i-1] + self.step

    def writetxt(self, filename='walk.txt'):
        f = open(filename, 'w')
        for i in range(self.n_points):
            f.write('{} {}\n'.format(self.time[i], self.pos[i]))
        f.close()
