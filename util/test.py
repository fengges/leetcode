def consumer():
    print("[Consumer] Init Consumer ......")
    r = "init ok"
    while True:
        # Consumer通过yield拿到消息，又通过yield把结果返回
        n = yield r
        print("[Consumer] conusme n = %s, r = %s" % (n, r))
        r = "consume %s OK" % n

def produce(c):
    print("[Producer] Init Producer ......")
    # 调用c.send(None)启动生成器
    r = c.send(None)
    print("[Producer] Start Consumer, return %s" % r)
    n = 0
    while n < 5:
        n += 1
        print("[Producer] While, Producing %s ......" % n)
        # 一旦生产了东西，通过c.send(n)切换到consumer执行
        r = c.send(n+100)
        print("[Producer] Consumer return: %s" % r)
    c.close()
    print("[Producer] Close Producer ......")

produce(consumer())