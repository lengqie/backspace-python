import backspace as bs
import time

bs.greeting()

bs_val = bs.Backspace().val
# print(bs_val.val)
# print("hello", bs_val,"world",sep="")
# print("hello", bs_val,"world",sep="")

# print(bs.n(-1))
# bs.loading()
kv = bs.KV()
kv.print()

test_list = ["单词", "撒旦", "但是", "赛弄得"]

print("key:", end=" ")
bs.printl(test_list, 2)
