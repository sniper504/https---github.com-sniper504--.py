class Birds:
    def __init__ (self,name,f_a,size):
        self.name = name
        self.f_a = f_a
        self.size = size



    def info_name(self):
        print(f"name:{self.name}")

    def eating(self):
        print("eating")

    def sounding(self):
        print("sounding")

    def sleeping(self):
        print(f"size:{self.size}")

    def flying_range(self, N):
        if self.f_a == True:
            print(f"f_a:{self.f_r}")

    def __del__ (self):
        print("del")


bird_1 = Birds("eagle",True,52)
bird_1.eating()
bird_1.sleeping()
N = 100
bird_1.flying_range(N)