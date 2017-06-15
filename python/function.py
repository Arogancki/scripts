import math

def podaj_dane():
    print('Podaj a')
    a=int(input())
    print('Podaj b')
    b=int(input())
    print('Podaj c')
    c=int(input())
    return a,b,c

def dodaj(d,x1r,x2r,x1u,x2u):
    if d > 0:
        rs=x1r+x2r
        us=0
    else:
        rs=x1r+x2r
        us=x1u+x2u
    return rs,us

def odejmij(d,x1r,x2r,x1u,x2u):
    if d > 0:
        rr=x1r-x2r
        ur=0
    else:
        rr=x1r-x2r
        ur=x1u-x2u
    return rr,ur

def pomnoz(d,x1r,x2r,x1u,x2u):
    if d > 0:
        ril=x1r*x2r
        uil=0
    else:
        ril=(x1r*x2r)-(x1u*x2u)
        uil=(x1r*x2r)+(x1r*x2u)
    return ril,uil

def podziel(d,x1r,x2r,x1u,x2u):
    rir=0
    uir=0
    if d > 0:
        if x2r != 0:
            rir=x1r/x2r
        else:
            rir=0
        uir=0
    else:
        if x2r != 0 or x2u != 0 :
            rir=( (x1r*x2r)+(x1u*x2u) ) / ( (x2r*x2r)+(x2u*x2u) )
            uir=( (x2r*x1u)-(x1r*x2u) ) / ( (x2r*x2r)+(x2u*x2u) )
    return rir,uir

def postac_trygonometryczna(a,d,x1r,x2r,x1u,x2u):
    if a != 0 and d < 0:
        fi1=0
        fi2=0
        m1=math.sqrt((x1r*x1r)+(x1u*x1u))
        m2=math.sqrt((x2r*x2r)+(x2u*x2u))
        if x1r !=0:
            fi1=math.atan(x1u/x1r)*(180.0/math.pi)
        if x2u !=0:
            fi2=math.atan(x2u/x2u)*(180.0/math.pi)
    else:
        m1=0
        m2=0
        fi1=0
        fi2=0
    return m1,m2,fi1,fi2

def oblicz_rownanie(a,b,c):
    d = oblicz_d(a,b,c)
    x1r=0
    x2r=0
    x1u=0
    x2u=0
    #oblicz rownanie
    if a != 0:
        if d > 0:
            x1r=(((float(b))*-1)-math.sqrt(d))/(2*(float(a)))
            x2r=((float(b)*-1)+math.sqrt(d))/(2*(float(a)))
            x1u=0
            x2u=0
        else:
            if d==0:
                x1r=(float(b)*(-1))/(2*(float(a)))
                x2r=0
                x1u=0
                x2u=0
            else:
                x1r=((-1)*float(b))/(2*float(a))
                x2r=x1r
                x1u=math.sqrt(math.fabs(d))/(float(2)*(float(a)))
                x2u=(x1u*(-1))
        return d,x1r,x2r,x1u,x2u
    elif b != 0:
        x1r=(float(c)*(-1))/(float(b))
        x2r=0
        x1u=0
        x2u=0
    return d,x1r,x2r,x1u,x2u

def oblicz_d(a,b,c):
    d=(b*b)-(4*a*c)
    return d

def formatuj_rownanie(a,b,c):
    #drukowanie a
    if a > 0:
        if a == 1:
            print('xx',end="")
        else:
            print(a,'xx',end="")
    elif a < 0:
        if a == -1:
            print('- xx',end="")
        else:
            print(a,'xx',end="")
    # else a == 0 nic nie drukuje
    #drukowanie b
    if b > 0:
        if b == 1:
            if a != 0:
                print(' + ',end="")
            print('x',end="")
        else:
            if a != 0:
                print(' + ',end="")
            print(b,'x',end="")
    elif b < 0:
        if b == -1:
            print('-x',end="")
        else:
            print(b,'x',end="")
    # else b == 0 nic nie drukuje
    #drukowanie c
    if c > 0:
        if b != 0 or a!= 0:
            print(' + ',end="")
        print(c,end="")
    elif c < 0:
        print(c,end="")
    # else c == 0 nic nie drukuje

    if a == 0 and b == 0 and c == 0:
        print ('0',end="")
    print (' = 0');
    
    return

def wyswietl(a,b,c,d,x1r,x2r,x1u,x2u,rs,rr,ilr,irr,us,ur,ril,uil,rir,uir,m1,m2,fi1,fi2):
    if a != 0:
        print ('d=',d)
        if d > 0:
            print ('x1r=',round(x1r,2),' x2r=',round(x2r,2))
            if x2r >= 0:
                print ('rs = ',round(rs,2),'=',round(x1r,2),'+',round(x2r,2))
                print ('rr = ',round(rr,2),'=',round(x1r,2),'-',round(x2r,2))
            else:
                print ('rs = ',round(rs,2),'=',round(x1r,2),'',round(x2r,2))
                print ('rr = ',round(rr,2),'=',round(x1r,2),'+',round((x2r*(-1)),2))
            print ('ilr = ',round(ilr,2),'=',round(x1r,2),'*',round(x2r,2))
            if x2r != 0:
                print ('irr = ',round(irr,2),'=',round(x1r,2),'/',round(x2r,2))
        else:
            if d < 0:
                if x1u < 0:
                    print (round(x1r,2),round(x1u,2),'*i')
                else:
                    print (round(x1r,2),'+',round(x1u,2),'*i')

                if x2u < 0:
                    print (round(x2r,2),round(x2u,2),'*i')
                else:
                    print (round(x2r,2),'+',round(x2u,2),'*i')

                if us >= 0:
                    print (round(rs,2),'+',round(us,2),'*i')
                else:
                    print (round(rs,2),round(us,2),'*i')

                if ur >= 0:
                    print (round(rr,2),'+',round(ur,2),'*i')
                else:
                    print (round(rr,2),round(ur,2),'*i')
                    
                if uil >= 0:
                    print (round(ril,2),'+',round(uil,2),'*i')
                else:
                    print (round(ril,2),round(uil,2),'*i')

                if uir >= 0:
                    print (round(rir,2),'+',round(uir,2),'*i')
                else:
                    print (round(rir,2),round(uir,2),'*i')
                    
                print (round(m1,2),'(cos(',round(fi1,2),')+i*sin(',round(fi1,2),'))')
                print (round(m2,2),'(cos(',round(fi2,2),')+i*sin(',round(fi2,2),'))')
            
            else: #d==0
                print (round(x1r,2),'=',round(x1r,2))
        return
    #a==0
    if b != 0:
        print('x1r=',round(x1r,2))
        return

    if c != 0:
        print ('Rownanie sprzeczne')
    else:
        print ('Rownanie tozsamosciowe')
	
    return


#main

a=0
b=0
c=0

a,b,c = podaj_dane()
formatuj_rownanie(a,b,c)
d,x1r,x2r,x1u,x2u = oblicz_rownanie(a,b,c)
rs,us=dodaj(d,x1r,x2r,x1u,x2u)
rr,ur=odejmij(d,x1r,x2r,x1u,x2u)
ilr,ilu=pomnoz(d,x1r,x2r,x1u,x2u)
irr,iru=podziel(d,x1r,x2r,x1u,x2u)
m1,m2,fi1,fi2=postac_trygonometryczna(a,d,x1r,x2r,x1u,x2u)
wyswietl(a,b,c,d,x1r,x2r,x1u,x2u,rs,rr,ilr,irr,us,ur,ilr,ilu,irr,iru,m1,m2,fi1,fi2)