
> It provides a standardized location for mounting and accessing various types of removable media

## **Things to know about `/media`:**

- ### **Automatic mounting**
    
    When a removable media device is connected to the system, the Linux operating system automatically mounts it under the `/media` directory. 
    
- ### **Manual mounting**
    
    Users can manually mount a device by using the `mount` command. 
    
- ### **Subdirectories**
    
    For each connected removable media device, a subfolder is automatically generated inside the `/media` directory. For example, a subdirectory for optical drives is `/media/cdrom`. 
    
- ### **Removing the device**
    
    When a removable media device is removed from the system, the associated subfolder is automatically deleted.