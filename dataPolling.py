from multiprocessing import Process
import Modules
for item in Modules.__all__:
        exec("from Modules import %s" %item)
        exec("Process(target=Modules."+item + ".run).start()")
