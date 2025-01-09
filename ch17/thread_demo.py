import threading, time

print('Start of program.')

def take_a_nap():
    time.sleep(5)
    print('Wake up!')


# To create a Thread object, we call threading.Thread() and pass it the
# keyword argument target=take_a_nap. This means the function we want to call
# in the new thread is takeANap(). Notice that the keyword argument is
# target=takeANap, not target=takeANap(). This is because you want to pass the
# takeANap() function itself as the argument, not call takeANap() and pass its
# return value.
thread_obj = threading.Thread(target=take_a_nap)
thread_obj.start()

print('End of program.')