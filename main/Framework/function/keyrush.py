def enable_copy_paste(entry):
    entry.bind("<Control-c>", lambda e: entry.event_generate("<<Copy>>"))
    entry.bind("<Control-v>", lambda e: entry.event_generate("<<Paste>>"))
    entry.bind("<Control-x>", lambda e: entry.event_generate("<<Cut>>"))
    entry.bind("<Control-a>", lambda e: entry.event_generate("<<SelectAll>>"))
