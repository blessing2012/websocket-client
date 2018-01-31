import websocket
import time
import sys


def on_message(ws, message):
    print(message)
    f.write(message)
    f.write(",\n")


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")
    f.write("]}")
    f.close()


def on_open(ws):
    print("### connected ###")
    f.write("{\"Data\":[\n")


if __name__ == "__main__":
    websocket.enableTrace(True)
    if len(sys.argv) < 2:
        host = "wss://www.bitmex.com/realtime?subscribe=quote:XBTUSD"
    else:
        host = sys.argv[1]
    f = open('quote'+time.strftime('%Y%m%d%H%M%S'+'.json', time.localtime(time.time())), 'w')
    ws = websocket.WebSocketApp(host,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
