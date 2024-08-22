def before_all(context):
    # Any setup before tests run
    pass

def after_all(context):
    if hasattr(context, 'browser'):
        context.browser.quit()
