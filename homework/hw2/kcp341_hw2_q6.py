def two_sum(srt_lst,target):
    #srt_lst = a list of integers arranged in a sorted order
    #target = an integer
    if len(srt_lst)==0:
        return None
    else:
        front_count = 0
        back_count = len(srt_lst)-1
        for i in range(len(srt_lst)):
            if back_count == front_count:
                return None
            else:
                if srt_lst[front_count] + srt_lst[back_count] == target:
                    return (front_count,back_count)
                elif srt_lst[front_count] + srt_lst[back_count] < target:
                    front_count+=1
                else:
                    back_count-=1

