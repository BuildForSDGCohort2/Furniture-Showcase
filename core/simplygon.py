from simplygon import simplygon_loader
from simplygon import Simplygon
import gc


def do_something(sg):
    # Do some processing using the SDK
    pass

# Initialize the SDK


sg = simplygon_loader.init_simplygon()

# Check if we got an error (sg is None) before continuing
if sg is None:
    # An error occured
    error = Simplygon.GetLastInitializationError()
    error_string = Simplygon.GetErrorString(error)
    sys.stderr.write('Initialization failed! {} (error {})\n'.format(error_string, error))
    # The printout above is also done internally by simplygon_loader
    # The code here is just an example on how to get information about the error

# Due to garbage collection in Python it's important that there is no Simplygon
# data that is allocated/deallocated in the same scope as the the deinitialization
# of Simplygon.
do_something(sg)

# To deinitialize Simplygon explicitly, assign None to the sg variable and then call
# Python's gc.collect() method to force a garbage collection pass
sg = None
gc.collect()
