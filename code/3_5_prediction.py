import numpy as np
import statsmodels.api as sm

F1 = np.loadtxt('3_5/feature_1_p1',delimiter=',')
F2 = np.loadtxt('3_5/feature_2_p2',delimiter=',')
F3 = np.loadtxt('3_5/feature_3_p3',delimiter=',')
F4 = np.loadtxt('3_5/feature_4_p1',delimiter=',')
F5 = np.loadtxt('3_5/feature_5_p1',delimiter=',')
F6 = np.loadtxt('3_5/feature_6_p2',delimiter=',')
F7 = np.loadtxt('3_5/feature_7_p3',delimiter=',')
F8 = np.loadtxt('3_5/feature_8_p1',delimiter=',')
F9 = np.loadtxt('3_5/feature_9_p2',delimiter=',')
F10 = np.loadtxt('3_5/feature_10_p3',delimiter=',')

F1=sm.add_constant(F1)
F2=sm.add_constant(F2)
F3=sm.add_constant(F3)
F4=sm.add_constant(F4)
F5=sm.add_constant(F5)
F6=sm.add_constant(F6)
F7=sm.add_constant(F7)
F8=sm.add_constant(F8)
F9=sm.add_constant(F9)
F10=sm.add_constant(F10)

D1 = np.loadtxt('3_5/next_1_p1',delimiter=',')
D2 = np.loadtxt('3_5/next_2_p2',delimiter=',')
D3 = np.loadtxt('3_5/next_3_p3',delimiter=',')
D4 = np.loadtxt('3_5/next_4_p1',delimiter=',')
D5 = np.loadtxt('3_5/next_5_p1',delimiter=',')
D6 = np.loadtxt('3_5/next_6_p2',delimiter=',')
D7 = np.loadtxt('3_5/next_7_p3',delimiter=',')
D8 = np.loadtxt('3_5/next_8_p1',delimiter=',')
D9 = np.loadtxt('3_5/next_9_p2',delimiter=',')
D10 = np.loadtxt('3_5/next_10_p3',delimiter=',')

n1Params=np.array([  1.27958012e+02,   8.53394878e-02,   2.95597415e-02,   1.90040400e+00])
n2Params=np.array([ -1.81960916e+03,   1.80790216e-01,  -6.61419007e-01,   1.62404171e+01])
n3Params=np.array([  3.05503584e+02,  -1.80871799e-01,   1.86474869e-01,  -6.66677145e-01])
s1Params=np.array([ 1.27050291,  0.07351563,  0.32799911, -1.13586267])
s2Params=np.array([  7.50273608e+03,   6.76986542e+00,  -3.63363797e-01,  -4.38255481e+01])
s3Params=np.array([  2.23587570e+02,  -6.44813828e-03,  -1.22968149e-01,   2.46702921e+00])

e1n = np.abs(np.dot(F1,n1Params)-D1)
e1s = np.abs(np.dot(F1,s1Params)-D1)
e2n = np.abs(np.dot(F2,n2Params)-D2)
e2s = np.abs(np.dot(F2,s2Params)-D2)
e3n = np.abs(np.dot(F3,n3Params)-D3)
e3s = np.abs(np.dot(F3,s3Params)-D3)
e4n = np.abs(np.dot(F4,n1Params)-D4)
e4s = np.abs(np.dot(F4,s1Params)-D4)
e5n = np.abs(np.dot(F5,n1Params)-D5)
e5s = np.abs(np.dot(F5,s1Params)-D5)
e6n = np.abs(np.dot(F6,n2Params)-D6)
e6s = np.abs(np.dot(F6,s2Params)-D6)
e7n = np.abs(np.dot(F7,n3Params)-D7)
e7s = np.abs(np.dot(F7,s3Params)-D7)
e8n = np.abs(np.dot(F8,n1Params)-D8)
e8s = np.abs(np.dot(F8,s1Params)-D8)
e9n = np.abs(np.dot(F9,n2Params)-D9)
e9s = np.abs(np.dot(F9,s2Params)-D9)
e10n = np.abs(np.dot(F10,n3Params)-D10)
e10s = np.abs(np.dot(F10,s3Params)-D10)

f=open('./3_5/result.txt','w')
f.write('nfl prediction'+'\n')
f.write(str(e1n)+'\n')
f.write(str(e2n)+'\n')
f.write(str(e3n)+'\n')
f.write(str(e4n)+'\n')
f.write(str(e5n)+'\n')
f.write(str(e6n)+'\n')
f.write(str(e7n)+'\n')
f.write(str(e8n)+'\n')
f.write(str(e9n)+'\n')
f.write(str(e10n)+'\n')
f.write('\n'+'superbowl prediction'+'\n')
f.write(str(e1s)+'\n')
f.write(str(e2s)+'\n')
f.write(str(e3s)+'\n')
f.write(str(e4s)+'\n')
f.write(str(e5s)+'\n')
f.write(str(e6s)+'\n')
f.write(str(e7s)+'\n')
f.write(str(e8s)+'\n')
f.write(str(e9s)+'\n')
f.write(str(e10s)+'\n')

f.close()







