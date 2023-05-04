# Logs 0.1 APLHA
### Just a logs module for Python

![logo 350](https://user-images.githubusercontent.com/90092906/236025011-d42c4ee8-624a-4656-92d5-5f120d49a18e.png)

Note: This module is updating every week, so be sure to check the updates frequently!

1. [Default values](https://github.com/FaserGer853/Logs/edit/main/README.md#default-values)
2. [How to use my module?](https://github.com/FaserGer853/Logs/edit/main/README.md#how-to-use-my-module)
3. [Conclusion](https://github.com/FaserGer853/Logs/edit/main/README.md#conclusion)

### Default values
```
logs.log(message='No response', path='\')
logs.warn(message='No response', path='\')
logs.error(message='No response', path='\')
logs.fatal(message='No response', code=1, path='\')
```



### How to use my module?

  Use ```logs.log()``` to display and save the log to the ```.log``` file.
Example:
```
message="Just a basic log"
logfile='\log\'
logs.log(message, log)
```

  There's also a warning log, that warns about something.
Example:
```
message="A warning about something"
logfile='\log\'
logs.warn(message, log)
```
  Same with the error log.
  
  Also, theres a fatal error, that requires: Message, error code and path.
 Example:
```
message="Fatal"
logfile='\log\'
logs.fatal(message, code=1, logfile)
```

## Conclusion

If you have more questions about usage, see the ```Issues``` page.
