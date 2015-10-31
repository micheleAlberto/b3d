from server import update

#minimal plugin
target_plugin='ping'

def setup():
    update(target_plugin,1)
    return __name__
def handle(data,status):
    next=status[__name__]+status[target_plugin]
    print '{} : {} @ {}',__name__,next,target_plugin
    update(target_plugin,next)
    #data is a json object
    pass
def clean():
    pass
