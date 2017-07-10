# import threading
# from wsgiref import simple_server
# # from selenium import webdriver
# # from my_application import model
# # from my_application import web_app

# def before_all(context):
#     # context.server = simple_server.WSGIServer(('', 8000))
#     # context.server.set_app(web_app.main(environment='test'))
#     context.thread = threading.Thread(target=context.server.serve_forever)
#     context.thread.start()
#     # context.browser = webdriver.Chrome()

# def after_all(context):
#     context.server.shutdown()
#     context.thread.join()
#     context.browser.quit()

# def before_feature(context, feature):
    # model.init(environment='test')