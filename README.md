# SHADCNPY

Toy port of shadcn to fast-html.

## How to develop
pip install -e .

## Example app
```python
from shadcn import *
from fasthtml.fastapp import *

data = [
  {
    "id": "TASK-8782",
    "title": "You can't compress the program without quantifying the open-source SSD pixel!",
    "status": "in progress",
    "label": "documentation",
    "priority": "medium"
  },
  {
    "id": "TASK-7878",
    "title": "Try to calculate the EXE feed, maybe it will index the multi-byte pixel!",
    "status": "backlog",
    "label": "documentation",
    "priority": "medium"
  },
]

columns = [
    {
        'header': lambda: Checkbox(),
        'cell': lambda x: Checkbox(),
    },
    {
        'header': lambda: 'Task',
        'accessor_key': 'id',
        'cell': lambda x: x['id'],
    },
    {
        'header': lambda: 'Title',
        'accessor_key': 'title',
        'cell': cell,
    },
    {
        'header': lambda: 'Status',
        'accessor_key': 'status',
        'cell': lambda x: Span(x['status'].title()),
    },
    {
        'header': lambda: 'Priority',
        'accessor_key': 'priority',
        'cell': lambda x: x['priority'].title(),
    },
]



@rt("/")
def get():
    return (
        Script(src="https://cdn.tailwindcss.com"),
        Body(
            Div(
                datatable(data=data, columns=columns),
                cls="h-full flex-1 flex-col space-y-8 p-8 md:flex"
            ),
            style='''-webkit-font-smoothing:antialiased; -moz-osx-font-smoothing:grayscale;''',
        ),
    )

serve()
```