
- ### **Pseudo-terminals**
    
    A pair of pseudo-device endpoints that establish a bidirectional communication channel between two or more processes. 
    
- ### **Special empty files**
    
    These include `/dev/null`, which discards all data written to it, and `/dev/full`, which always returns a “disk full” error when written to. 
    
- ### **Special files that return a stream of data**
    
    These include `/dev/zero`, which returns an infinite stream of null bytes, and `/dev/random` and `/dev/urandom`, which return an infinite stream of random data. 
    
- ### **Virtual terminals**
    
    These include `/dev/tty*`, which is used to interact with the system, and `/dev/pts* which is used to create virtual terminals. 
    
- ### **Shared memory segments**
    
    These include `/dev/shm*`, which is used by the kernel to share data between processes. 
    
- ### **Standard input, output, and error streams**
    
    These include `/dev/stdin`, `/dev/stdout`, and `/dev/stderr`, which are used to redirect input and output.