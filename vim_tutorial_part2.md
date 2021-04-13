# Vim Tutorial Part 2

(Disclaimer, some of this tutorial is based off vimtutor!)






## 1. Moving to the start and end (0$)

To move to the start of the line, press `0`.
To move to the end   of the line, press `$`.


Lorem Ipsum is simply dummy text of the printing and typesetting industry.



























## 2. Enter insert mode at start and end (IA)

To enter insert mode at the start of the line, press `I`.
To enter insert mode at the end   of the line, press `A`.


Lorem Ipsum is simply dummy text of the printing and typesetting industry.



























## 3. Open line before and after current line (oO)

To open a new line below and enter insert mode, press `o`.
To open a new line above and enter insert mode, press `O`.


Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
when an unknown printer took a galley of type and scrambled it to make a type specimen book.
It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.
It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, 
and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.






















## 4. Navigating to the start, end and a specific line number (g_)

To go to the start of the file,  press `gg`.
To go to the end of the file,    press `G`.
To go to a specific line number, press `#G`

Tip: `ctrl-o` and `ctrl-i` takes you to your cursor's previous and future jumps respectively.



























## 5. Horizontal movement (tfTF;,)

To navigate forwards  till a specific letter, press `t_` where `_` is the letter. 
To navigate backwards till a specific letter, press `T_` where `_` is the letter. 

To navigate forwards  to   a specific letter, press `f_` where `_` is the letter. 
To navigate backwards to   a specific letter, press `F_` where `_` is the letter. 

To go to the next     entry, press `;`.
To go to the previous entry, press `,`.


Lorem Ipsum is simply dummy text of the printing and typesetting industry.  Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.  It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.  It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.





















## 6. Find

To search for a phrase (regex), press `/<search term>`.

To go to the next     entry, press `n`.
To go to the previous entry, press `N`.

To search for the next     word the cursor is on, press `*`.
To search for the previous word the cursor is on, press `#`.

























## 7. The foundations to the "power" of Vim

Now we finally get a very interesting milestone in Vim usage. We can now start to form "sentences" in Vim. 

(The following from: https://danielmiessler.com/study/vim/)
Verb - Modifiers - Nouns

### Verbs:
- d: delete
- c: change
- y: yank
- v: visual

### Modifiers:
- i: inside
- a: around
- NUM: number (e.g. 1, 2, 3...)
- t: till
- f: find to

### Nouns:
- w: word
- s: sentence
- p: paragraph
- t: tags (e.g. <div></div>)
- b: block
- ": double quotes
- ': single quotes
- (: braces
- {: curly braces
- [: square braces


E.g.

1. 
The quick brown fox jumped over the lazy dog.

2. 
ser = Serial.begin(int(input('Enter a COM port')))

3. 
<div>
  <span>
    Testing
  </span>
</div>

4. 

10/04/2020,VISA PURCHASE   PAYPAL *UBER AU 4029357733   08/04 AU AUD,-$34.79,$86.05


5. Can also do <num><hjkl>!














## 8. Macros, the true "power" of Vim.

To start recording a macro, press `q_`, where `_` is a register.
To stop  recording a macro, press `q`.

To play back a macro, press `@_`, where `_` is a register.




























# 9. An example program!

Hailstones? 







