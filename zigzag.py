import time, sys
indent = 0 # How many spaces to indent.
indentIncreasing= True # Whether the indentation is increasing or not.

try:
    while True: # main loop
        print(' ' * indent, end=' ')
        print('********')
        time.sleep(0.1) # Pausing for 1/10 a sec.

        if indentIncreasing:
            # Increasing the number of spaces
            indent = indent + 1
            if indent == 20:
                # Change direction
                indentIncreasing = False
        else:
            indent = indent - 1
            if indent == 0:
                    # Change direction
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()
      
