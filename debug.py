import json
from ws4py.client.threadedclient import WebSocketClient




class CG_Client(WebSocketClient):

    def opened(self):
        # req = '{"event":"subscribe", "channel":"eth_usdt.deep"}'
        req = '{"message":"subscribe"}'
        self.send(req)

    def closed(self, code, reason=None):
        print("Closed down:", code, reason)

    def received_message(self, resp):
        resp = json.loads(str(resp))
        data = resp['message']
        print(data)
        if type(data) is dict:
            ask = data['asks'][0]
            print('Ask:', ask)
            bid = data['bids'][0]
            print('Bid:', bid)
        if data:
            # self.closed(code=1000,reason='data received successful')
            self.close_connection()

if __name__ == '__main__':
    ws = None
    try:
        ws = CG_Client('ws://127.0.0.1:8000/ws/chat/b/')
        ws.connect()
        ws.run_forever()
    except KeyboardInterrupt:
        ws.close()