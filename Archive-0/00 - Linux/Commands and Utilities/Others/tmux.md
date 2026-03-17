
> [!note] 
> These commands follows key bindings defined in <mark style="background: #ABF7F7A6;">oh-my-tmux</mark>

</br>

## <mark style="background: #D2B3FFA6;">Sessions</mark>

### Open a new named session
```bash ln:False
$ tmux new -s "session-name"
```

### Rename session
```bash ln:False
<Ctrl-a> + $
```


### Detach Session (<mark style="background: #CACFD9A6;">exit and keep running in background</mark>)
```bash ln:False
<Ctrl-a> + d
```

### List Sessions
```bash ln:False
$ tmux ls
```
*OR*
```bash ln:False
<Ctrl-a> + s
```

### Attach Session
```bash ln:False
$ tmux attach-session -t "session-name"
```
*OR*
- attach to the most recently used session
```bash ln:False
$ tmux attach
```

### Kill Session
```bash ln:False
<Ctrl-a> + :kill-session
```

---

</br>

# <mark style="background: #BBFABBA6;">Windows</mark>

### Open a new window
```bash ln:False
<Ctrl-a> + c
```

### Rename window
```bash ln:False
<Ctrl-a> + ,
```

### Close window
```bash ln:False
<Ctrl-a> + &
```

### Navigate Window
- navigate by window number
```bash ln:False
<Ctrl-a> + [0-9]
```
- navigate to the last used window
```bash ln:False
<Ctrl-a> + <Tab>
```
- navigate to the previous window
```bash ln:False
<Ctrl-a> + <Ctrl-h>
```
- navigate to the next window
```bash ln:False
<Ctrl-a> + <Ctrl-l>
```

---

</br>

# <mark style="background: #FFB86CA6;">Panes</mark>

## Show Pane Numbers
```bash ln:False
<Ctrl-a> + q
```

### Horizontal Split (_)
```bash ln:False
<Ctrl-a> + _
```

### Vertical Spliot (-)
```bash ln:False
<Ctrl-a> + -
```

### Close active pane
```bash ln:False
<Ctrl-a> + x
```

### Evenly space all panes
```bash ln:False
<Ctrl-a> + E
```

### Show time on the active pane
```bash ln:False
<Ctrl-a> + t
```

### Zoom active pane
```bash ln:False
<Ctrl-a> + z			# Press it again to zoom out
```


---

</br>

# <mark style="background: #FFF3A3A6;">Mouse</mark>

### Enable mouse for scrolling
- Unable to select text after scrolling
```bash ln:False
<Ctrl-a> + m
```


### Alternatively (Scroll using arrow keys)
- able to select text after scrolling

```bash ln:False
<Ctrl-a> + [
```