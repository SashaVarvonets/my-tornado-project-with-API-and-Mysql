import tornado.web
import tornado.ioloop

from torndb_connector import DbConnector
from handlers import DefaultDataHandler

if __name__ == "__main__":

    application = tornado.web.Application([
        (r"/", DefaultDataHandler, dict(db=DbConnector()))
    ])

    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
