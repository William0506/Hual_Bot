import time

def ping (time1,command):
    if command == "ping":
        time2 = time.time()
        timer = round(time2-time1,6)
        return f"Pong! 延遲時間為: {timer} 秒"