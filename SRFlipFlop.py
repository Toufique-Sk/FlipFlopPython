class Gates:
    def NAND(self,A,B):
        return not(A and B)

class FlipFlop:
    def flFp(self,A,B,Q=0):
        nandQ=Gates()
        nandNotQ=Gates()
        notQ=nandNotQ.NAND(Q,B)
        Q=nandQ.NAND(A,notQ)
        notQ=nandNotQ.NAND(Q,B)
        return Q,notQ

class SR:
    def setReset(self,A,B,clk=1):
        srFlFp=FlipFlop()
        Nand=Gates()

        outA=Nand.NAND(A,clk)
        outB=Nand.NAND(B,clk)
        Q,notQ=srFlFp.flFp(outA,outB)
        return Q,notQ

sr=SR()
while 1:
    print "Enter A B"
    A,B=map(int,raw_input().split())
    Q,notQ=sr.setReset(A,B)
    if Q==notQ:
        print "Invalid State"
    elif A==0 and B==0:
        print "No change state"
    else:
        print "A        B"
        print "----------"
        print str(Q)+" "+str(notQ) 
        
