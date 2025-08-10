import justpy as jp

def quazar1():
    wp = jp.QuasarPage() # we create QuasarPage(class) object
    #QDiv components of the web app.
    head1 = jp.QDiv(a=wp, text="This is a simple web app", classes="text-h1 text-center q-pt-xs")
    para1 = jp.QDiv(a=wp, text="This graph presents ratings of courses")
    return wp

#Now, we need a function call to create and access the quasar page.
jp.justpy(quazar1) # Expects a function which returns a qausar page as its input.