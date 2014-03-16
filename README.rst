===============================
ftpext
===============================

Extensions to the 'ftplib' library.

* Documentation: http://ftpext.rtfd.org.
* GitHub: https://github.com/kalind/ftpext
* Free software: BSD license



Features
--------

* Stat -L directory listing support.
* FXP support (CPSV/PSV).
* Logging and other useful features, have a look yourself.
* PRET support.
* X-DUPE support.
    
I've made the getter functions thread-safe to make multiple objects
easier to handle.
It inherits from ftplib.FTP_TLS which means that it supports both
normal FTP and FTPS protocol, which one to use is specified when the object is
created.

Check documentation for full info.
