# Vim Tutorial Part 1

(Disclaimer, some of this tutorial is based off vimtutor!)












## 1. How to open and close vim.

- To start Vim, type `vim [filename]` in the terminal! You are in normal mode!
- To close Vim, type `:q` in Vim!






























## 2. Basic movement (hjkl)

Use hjkl to move (left, down, up, right)! Don't use your arrow keys!!!!!!! (If you do, you'll be banished from SYNCS)



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






















## 7. Undo and redo

Unlike ctrl-z and ctrl-shift-z, in vim it is `u` and `ctrl-r`! The shortcuts make sense and save you a few keystrokes! 

Happy hands happy girlfriend!



Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
when an unknown printer took a galley of type and scrambled it to make a type specimen book.
It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.
It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, 
and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.




















## 8. Yank and paste

Copy pasting in Vim is different! We "yank" and "paste". 

To copy a line, press `yy`. To paste the line, press `p`.



Copy me!!!

























## 9. Visual mode (v)


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














## 10. A great way to practise, Vim-Be-Good!

A game to train your fundamentals!



