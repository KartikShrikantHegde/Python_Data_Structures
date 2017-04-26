Why isnumeric on strings works only for ascii ot utf-8 ??


Often you will want to check if a string in Python is a number.
This happens all the time, for example with user input,
fetching data from a database (which may return a string),
or reading a file containing numbers. Depending on what type of number you are expecting,
you can use several methods. Such as parsing the string, using regex,
or simply attempting to cast (convert) it to a number and see what happens. Often you will also encounter non-ASCII numbers, encoded in Unicode. These may or may not be numbers. For example ๒, which is 2 in Thai. However © is simply the copyright symbol, and is obviously not a number.