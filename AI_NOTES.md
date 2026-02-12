AI_NOTES.md :

AI tools were used only for very small guidance during development  mostly to quickly clarify a few technical points.

For example:
 Checking a couple of Flask routing patterns
 Confirming correct Git commands while pushing to GitHub
 Minor suggestions for improving structure and formatting

The main logic, structure, and implementation were done independently.

I designed and built:

 The database schema (transcripts + tasks)
 All Flask routes and request handling and CRUD operations for tasks
 Transcript parsing logic for action item extraction
 Filtering system 
 Last 5 transcript history feature
 Git repository setup 

All functionality was manually tested before pushing any code, I reviewed it carefully to ensure I fully understood how it works.
LLM Usage in the Application :
This version does not use a live LLM API Instead, I implemented a simple rule-based extraction approach (detecting keywords like "will") to identify action items.  
This keeps the application lightweight, easy to host, and free from external API dependencies.
The structure allows future integration of an LLM if needed.