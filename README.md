# Logs 0.1 APLHA
### Just a logs module for Python

![logo 350](https://user-images.githubusercontent.com/90092906/236025011-d42c4ee8-624a-4656-92d5-5f120d49a18e.png)

```Note: This module is updating every week, so be sure to check the updates frequently!```

1. [Default values](#Default values)
2. [How to use my module?](#How to use my module?)
3. [Practice](#Practice)

### Default values
```
logs.log(message='No response')
logs.warn(message='No response')
logs.error(message='No response')
logs.fatal(message='No response', code=1)
```



### How to use my module?

Use ```logs.log()``` to display and save the log to the ```.log``` file.
Example:
```
message="Just a basic log"
logs.log(message)
```

There's also a warning log, that warns about something.
Example:
```
message="A warning about something"
logs.warn(message)
```
