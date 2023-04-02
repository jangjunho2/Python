# hasing #해싱에서 많이 쓰이는 hornersrule
def horners_rule(text):
    total = 0
    nums = [ord(i)-96 for i in text]
    for i in range(len(text)):
        total += nums[i]*(31**i)
    return total


if __name__ == "__main__":
    m = input()
    result = horners_rule(m)
    print(result)
