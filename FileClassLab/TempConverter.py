class TempConverter:
    def c_to_f(self,c):
        return round((9/5)*c+32,1)

    def f_to_c(self,f):
        return round((5/9)*(f-32),1)

if __name__ == '__main__':
    tc = TempConverter()
    print(f"56F is {tc.f_to_c(56)}C")
    print(f"21C is {tc.c_to_f(21)}F")
