from collections import deque, defaultdict

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])
        ori_word_dict = defaultdict(int)
		
        for word in words:
            ori_word_dict[word] += 1
        
        all_word_len = len(words) * word_len
        result = []
        for i in range(word_len):
            queue = deque()
            word_dict = ori_word_dict.copy()
            for j in range(i, len(s) - word_len + 1, word_len):
                word = s[j:j + word_len]
                if word_dict.get(word, 0) != 0:
                    word_dict[word] -= 1
                    queue.append(word)
                    if sum(word_dict.values()) == 0:
                        result.append(j - all_word_len + word_len)
                        last_element = queue.popleft()
                        word_dict[last_element] = word_dict.get(last_element, 0) + 1
                else:
                    while len(queue):
                        last_element = queue.popleft()
                        if last_element == word:
                            queue.append(word)
                            break
                        else:
                            word_dict[last_element] = word_dict.get(last_element, 0) + 1
                            if word_dict[last_element] > ori_word_dict[last_element]:
                                word_dict = ori_word_dict.copy()

        return result
# class Solution:
#     def findSubstring(self, s: str, words: List[str]) -> List[int]:
#         result=[]
#         start_idx=0
#         last_idx=len(words[0])*len(words)
        
#         while last_idx<=len(s):
#             words_copy=words[::]
#             print("start_idx:",start_idx)
#             print("last_idx:",last_idx)
            
#             check_words=s[start_idx:last_idx]
#             for i in range(len(words)):
#                 # length = start_idx+(i*len(words[0]))
#                 # check=check_words[length:length+len(words[0])]
#                 length = i*len(words[0])
#                 check=check_words[length:length+len(words[0])]
#                 print("check_words:",check_words)
#                 print("length:",length)
#                 print("length+len(words[0]):",length+len(words[0]))
#                 print("check:",check)
                
#                 if check in words_copy:
#                     words_copy.remove(check)
#                 else:
#                     break
#             if len(words_copy)==0:
#                 result.append(start_idx)
            
#             start_idx+=len(words[0])
#             last_idx+=len(words[0])
#             print("\n")
#         return result
        