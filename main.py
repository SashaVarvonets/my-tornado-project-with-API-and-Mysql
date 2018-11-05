if __name__ == "__main__":
    from mysql_db_conector import db
    import tornado.ioloop
    from handlers import DefaultDataHandler
    import tornado.web


    application = tornado.web.Application([
        (r"/", DefaultDataHandler, dict(db=db))
    ])
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
