import tornado.web
import tornado.ioloop

from torndb_conector import my_db
from handlers import DefaultDataHandler

if __name__ == "__main__":

    application = tornado.web.Application([
        (r"/", DefaultDataHandler, dict(db=my_db))
    ])

    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
