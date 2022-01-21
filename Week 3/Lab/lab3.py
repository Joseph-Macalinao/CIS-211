import logging
logging.basicConfig(filename='/Users/josephmacalinao/PycharmProjects/CIS-211/Week 3/Lab/log.txt', level=logging.INFO)
log = logging.getLogger(name='MyFirstLog')
log.debug("Phew, made it through.")
log.error("Something is very wrong!")
log.info("This is just FYI")

print(log)

'''
to save log messages, change second line slightly, giving filename
and minimum level for saving messages
-> logging.basicConfig(filename = 'log.txt', level = logging.INFO)

Levels of Severity
┌──────────┬───────┐
│  Level   │ Value │
├──────────┼───────┤
│ CRITICAL │    50 │
│ ERROR    │    40 │
│ WARNING  │    30 │
│ INFO     │    20 │
│ DEBUG    │    10 │
└──────────┴───────┘

can specify any level with log.log()
'''

