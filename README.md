# Barcode alarm productivity
Make better use of barcode alarms and literally force yourself to do something productive :)


## The idea behind
There are many alarm apps with the barcode-scanning functionality: the alarm won't turn off, until you scan a specific barcode.

### ![Barcode alarm apps](barcode-alarm-apps.png)

Of course, having to walk to another room - to scan the barcode - might be sufficient to wake yourself up. However, it rather won't force you to start doing a specific activity. 
<br>

### Unless...
**...unless the barcode won't show up until you actually start doing it! ;)**


## Coding
Thanks to the script below, the barcode is generated when Python detects that you've been coding for some time.

### [check-if-coding.py](check-if-coding.py)

How it works: it reads what you're typing on your keyboard, and counts how many times programming-specific keys were clicked.
~~~python
programming_chars = {'{', '}', '(', ')', '=', '.', '<', '>', ';', 'space', 'shift', 'tab', 'ctrl', 'tab', 'enter'}
~~~

Once they've been clicked enough times, it creates an image file with barcode, opens it and delets it right after _(so that you won't be cheating)_.


## Meditation
...
### [barcode-after-meditation.html](barcode-after-meditation.html)
