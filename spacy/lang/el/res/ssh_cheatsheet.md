# Screens

1. List all active screens:
` screen -ls `
2. Starting new screen session:
`screen -S screen_name`
3. Connect to existing screen session:
`screen -r screen_name` 
4. Detaching from screen: Control + A + D
5. Kill screen: attach to it and then `exit`
Or: `screen -X -S [session # you want to kill] quit`

