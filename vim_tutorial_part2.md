# Vim Tutorial Part 2

(Disclaimer, some of this tutorial is based off vimtutor!)


- (gg)G
- tfTF;,

- ctrl-f ctrl-b ctrl-u ctrl-b
- Replace
- HML(zz)

- Numbers

- (cdyv)(iatfTF)("'(){}[]t)


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






















## 3. Insert mode (i)

To actually type text, press `i` to enter "insert mode".

To return to normal mode, press `esc` or `ctrl + c` or `ctrl + [`.


---> There is text misng this .
---> There is some text missing from this line.























## 4. Saving your changes (:w)

To save a file, type `:w`!





























## 5. Basic word movement (wb)

Press `w` to move forward a "word" and press `b` to move backwards a "word"!


Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
when an unknown printer took a galley of type and scrambled it to make a type specimen book.
It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.
It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, 
and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.





















## 6. Deleting characters and lines

Use `x` to delete a character in normal mode. 

Use `dd` to delete the current line!


** Delete me! **
** Delete me! **

** Deloitte me! **
** Deloitte me! **




















## 7. Yank and paste

Copy pasting in Vim is different! We "yank" and "paste". 

To copy a line, press `yy`. To paste the line, press `p`.



Copy me!!!























## 8. Visual mode (v)


To select a portion of text,   press `v`      to enter "visual" mode! 
To select rows      at a time, press `V`      to enter "visual-line" mode!
To select columns   at a time, press `ctrl-v` to enter "visual-block" mode!

Your normal navigation keys work here (hjklwb)!

You can then yank or delete your selection!

To re-select the last selection, press `gv`!


Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
when an unknown printer took a galley of type and scrambled it to make a type specimen book.
It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.
It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, 
and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.




