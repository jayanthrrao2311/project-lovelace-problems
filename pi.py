def almost_pi(N):
   temp = 0
   for i in range(N):
        temp = temp + ((-1)**i) / (2*i + 1)
   return temp * 4