# original_1:
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        
        

        index_same = []
        index_have = []
        secret_ori = list(secret)

        for i in range(len(secret)):

            if guess[i] == secret[i]:
                index_same.append(i)
                secret_ori.remove(guess[i])

            elif guess[i] in secret:

                index_have.append(guess[i])
                # secret_ori.remove(guess[i])

        B = 0

        for i in index_have:
            if i  in secret_ori:
                B += 1
                secret_ori.remove(i)


        # res = []
        # [res.append(x) for x in index_have if x not in res]

        # output = '%sA%sB' %(len(index_same), len(res))
        
        return '%sA%sB' %(len(index_same), B)
    
# original_2:
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        
        

        Bulls  = 0
        Cows = 0
        secret_ori = list(secret)
        guess_ori = list(guess)

        for i in range(len(secret)):

            if guess[i] == secret[i]:
                Bulls += 1
                secret_ori.remove(guess[i])
                guess_ori.remove(guess[i])


        for i in range(len(secret_ori)):

            if guess_ori[i]  in secret_ori:
                print(guess_ori[i])
                Cows += 1
                secret_ori.remove(guess_ori[i])



        return '%sA%sB' %(Bulls, Cows)
    
# God
class Solution:
    def getHint(self, secret, guess):
        lst_secret, lst_guess = list(secret), list(guess)
        i = bulls = cows = 0
        while i < len(lst_secret):
            if lst_secret[i] == lst_guess[i]:
                bulls += 1
                lst_secret.pop(i)
                lst_guess.pop(i)
            else:
                i += 1
        s_cnt, g_cnt = Counter(lst_secret), Counter(lst_guess)
        for c in s_cnt:
            if c in g_cnt:
                cows += min(s_cnt[c], g_cnt[c])
        return '%sA%sB' %(bulls, cows)