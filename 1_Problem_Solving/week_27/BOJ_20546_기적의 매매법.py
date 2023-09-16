import sys

input = sys.stdin.readline

money = int(input())
stocks = list(map(int, input().split()))

bnp = {"money": money, "stock": 0, "result": 0}
timing = {"money": money, "stock": 0, "result": 0}

for i in range(len(stocks)):
    # 준현이의 BNP 매매법
    # 구매 가능하다면 즉시 매수
    bnp["stock"] += bnp["money"] // stocks[i]
    bnp["money"] = bnp["money"] % stocks[i]

    # 성민이의 33 매매법
    # 3일 연속 전일 대비 상승했고,
    if (
        i > 2
        and stocks[i] > stocks[i - 1]
        and stocks[i - 1] > stocks[i - 2]
        and stocks[i - 2] > stocks[i - 3]
    ):
        if timing["stock"] > 0:  # 구매한 주식이 존재한다면
            timing["money"] += timing["stock"] * stocks[i]  # 전량 매도
            timing["stock"] = 0
    # 3일 연속 전일 대비 하락했다면
    elif (
        i > 0
        and stocks[i] < stocks[i - 1]
        and stocks[i - 1] < stocks[i - 2]
        and stocks[i - 2] < stocks[i - 3]
    ):
        timing["stock"] += timing["money"] // stocks[i]  # 전량 매수
        timing["money"] = timing["money"] % stocks[i]

bnp["result"] = bnp["money"] + bnp["stock"] * stocks[-1]
timing["result"] = timing["money"] + timing["stock"] * stocks[-1]

# print(bnp["result"], timing["result"])
if bnp["result"] > timing["result"]:
    print("BNP")
elif bnp["result"] < timing["result"]:
    print("TIMING")
else:
    print("SAMESAME")
