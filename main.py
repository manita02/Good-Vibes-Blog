from goodvibesblog import app, bd


#if __name__ == '__main__': #entrypoint
 #   app.run()


if __name__ == "__main__":
    with app.app_context():
        bd.create_all()
        app.run()
        