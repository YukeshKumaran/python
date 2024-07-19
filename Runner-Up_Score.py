if __name__ == '__main__':
    n = int(input())
    score= list(map(int, input().split()))   
    a= max(score) 
    c=score.count(a)
    for i in range(c):
        score.remove(a)
    print(max(score))
