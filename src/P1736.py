class Solution:
    def maximumTime(self, time: str) -> str:
        lst = list(time)

        if lst[0] == '?':
            if lst[1] == '?':
                lst[0] = '2'
            elif int(lst[1]) > 3:
                lst[0] = '1'
            else:
                lst[0] = '2'
        if lst[1] == '?':
            if lst[0] == '0':
                lst[1] = '9'
            elif lst[0] == '1':
                lst[1] = '9'
            else:
                lst[1] = '3'
        if lst[3] == '?':
            lst[3] = '5'
        if lst[4] == '?':
            lst[4] = '9'

        return ''.join(lst)