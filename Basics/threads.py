import threading
import time


# A daemon thread is a thread that does not prevent the JVM from exiting when
# the program finishes but the thread is still running. An example for a daemon
# thread is the garbage collection.
# if main thread exiting the code, main thread will not wait for daemon thread to complete

