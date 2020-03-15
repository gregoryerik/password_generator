# Password Generator

Module to generate secure passwords of particular length and/or characteristics.

## Usage

To create a password with three random words from the words.txt file:
```python
>>> pwd_worded = passwordWorded()
>>> print(pwd_worded) # E.g. adeption_siksika_430_melodium_400_971
```

To create a password which is completely random with characters, digits and punctuation:
```python
>>> pwd_random = passwordRandom()
>>> print(pwd_random) # E.g. <lZ'f^zy|7P>Hh>%
```
## Random Password
The Random Password generator has two optional parameters:
- Length
- Exclude

The length param will dictate the length of the password. By default it is 16.
The exclude param is a list which is not to be included. E.g. if ```[1,2,3,4]``` was entered, it will create a password without the opportunity to randomly select 1, 2, 3 or 4. 

## Worded Password
The Worded Password generator has two optional parameters:
- Word Count
- Number Count

The word count param will determine how many random words to put into the password. Defaults to 3.
The number count param will determine how many sets of 3 digit numbers to put into the password. Defaults to 3. 