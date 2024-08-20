But in python we nhave some assistant which always running in the background to destroy useless object.Because the chance pf failingg python program memory problems is very less.This assistant is nothing but garbagr collector.
If an object does not have any refrence variable then that object eligible for garbage collection.
By default garbage collector is enabled but we can disabled on our requirement.
In this context we can use the funtions enable(),disable() of gc module.
Destructor:
-----------
Destructoris a special method and the name should be _del_()just before Destroying an object GC always calls Destructor to perform clean up activities (Resoures deallocation activities like clos data base connecxtion etc)

