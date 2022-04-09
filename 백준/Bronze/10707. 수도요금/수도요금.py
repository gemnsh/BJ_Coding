A=int(input())
B=int(input())
C=int(input())
D=int(input())
P=int(input())
Y=B if P<=C else B+(P-C)*D
print(min(A*P,Y))