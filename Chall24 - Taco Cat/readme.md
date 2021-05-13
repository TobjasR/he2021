[chall24.png](chall24.png)

## Taco Cat
Was it a cat I saw?

[tacocat.zip](tacocat.zip)
### Hint:
lowercase

## Solution
* interpreting the hint in the challenge title, title pic and ziped file **eggge.png**: somthing about **palindromes** maybe?!
* extract hash from encrypted zip file with zip2john -> [tacocat.hash](tacocat.hash)
* trying to crack it with rockyou.lst fails…
* then we have to try more sophisticated bruteforce with palindroms 
* generate wordlists with alphanumeric lowercase strings; one with length 3, one with length 4 and one with 5 (6 would've been overkill, right?) -> [tacocat.lst](tacocat.lst)
* now comes the tricky part:

### John Rules

in ```john/john.conf``` (for e.g. 9 and 10 letter palindromes) append the following rules at the end:
```
# End of john.conf file.
# Keep this comment, and blank line above it, to make sure a john-local.conf
# that does not end with \n is properly loaded.
[List.Rules:palindromes]
f
f D5
```
then wen can run john with the wordlist plus the newly created "palindromes" rules like this:
```bash
$ john --wordlist=tacocat.lst --rules:palindromes tacocat.hash 
```
rule ```f``` simply appends a reflection of itself to the current word from the wordlist, e.g. passw -> passwwssap

rule ```f D5``` not only reflects the word but then deletes the 5th character, e.g. passw -> passwssap

Possible solution to "delete the middle character" (for variable word length):
```
f
Mr[6
```
```M``` = Memorize current word, ```r``` = Reverse the entire word , ```[``` = Delete first character, ```6``` = Prepend the word saved to memory to current word

With this approach the palindromes could additionally be "turned inside out" (word from wordlist at the end of the resulting palindrome instead of at beginning)
```
f   
Mr[6
Mr]4
```
```M``` = Memorize current word, ```r``` = Reverse the entire word , ```]``` = Delete last character, ```4``` = Append the word saved to memory to current word

#### result
```bash
$ john --wordlist=tacocat.lst --rules:tacocat tacocat.hash 
Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
Will run 6 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
mousesuom        (tacocat.zip/eggge.png)
1g 0:00:00:01 DONE (2021-04-16 14:23) 0.6993g/s 4021Kp/s 4021Kc/s 4021KC/s momxkxmom..mpfbzbfpm
Use the "--show" option to display all of the cracked passwords reliably
Session complete
```
so, it found zip password **mousesuom**
with this we can extract the [eggge.png](eggge.png)
