

def TOHElapsed(A,C,B,height,elapsedTime):
    if (height >=1):

        TOHElapsed(A,B,C,height-1,elapsedTime)
        print("disk", height, ":", A, "to", C)

        if(A=="SRC" and C=="DST") or (A=="DST" and C=="SRC"):
            elapsedTime[height - 1] = elapsedTime[height - 1] + height * 2
        else:
            elapsedTime[height - 1] = elapsedTime[height - 1] + height * 1

        TOHElapsed(B,C,A,height-1,elapsedTime)


def towers(A,B,C,height):
    j=1
    elapsed = [0]*height
    TOHElapsed(A,C,B,height,elapsed)
    for i in elapsed:
        print("Elapsed time for disk",j,":",i)
        j=j+1

towers("SRC","AUX","DST",4)