def before_all(context):

    pass

def after_all(context):
    if hasattr(context, 'browser'):
        context.browser.quit()
