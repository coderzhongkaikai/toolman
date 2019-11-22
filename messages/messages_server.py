import tornado.ioloop
import tornado.web
import json
from . import handler


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")
        self.write('ok')

    def post(self):
        data = json.loads(self.request.body, encoding='utf-8')
        print(data)
        self.write('ok')
        handler.handler(data)


def run():
    application = tornado.web.Application([
        (r"/", MainHandler),
    ])
    application.listen(9004)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    run()
