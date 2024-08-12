from functools import partial
from typing import Any, Callable, TypedDict
from fasthtml.components import ft_hx, Div, Span, Table, Thead, Tbody, Tr, Th, Td


Svg = partial(ft_hx, "svg")
Pth = partial(ft_hx, "path")


class ColumnSpec(TypedDict):
    header: Callable[[], str]
    accessor_key: str
    cell: Callable[[dict[str, Any]], Any]


def badge(*x, cls=""):
    return Div(
        *x,
        cls="inline-flex items-center rounded-md border px-2.5 py-0.5 text-xs font-semibold transition-colors focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 text-foreground "
        + cls,
    )


def cell(x):
    return Div(
        badge(x["label"].capitalize()) if "label" in x else "",
        Span(x.get("title"), cls="max-w-[500px] truncate font-medium"),
        cls="flex space-x-2",
    )


def tablecell(*x, cls=""):
    return Td(
        *x,
        cls="p-2 align-middle [&:has([role=checkbox])]:pr-0 [&>[role=checkbox]]:translate-y-0.5 "
        + cls,
    )


def th(*x, cls=""):
    return Th(
        *x,
        cls="h-10 px-2 text-left align-middle font-medium text-muted-foreground [&:has([role=checkbox])]:pr-0 [&>[role=checkbox]]:translate-y-0.5 "
        + cls,
    )


def tablerow(*x, cls=""):
    return Tr(
        *x,
        cls="border-b transition-colors hover:bg-muted/50 data-[state=selected]:bg-muted "
        + cls,
    )


def table(*x, cls=""):
    return Div(
        Table(*x, cls="w-full caption-bottom text-sm " + cls),
        cls="relative w-full overflow-auto",
    )


def thead(*x, cls=""):
    return Thead(*x, cls="[&_tr]:border-b " + cls)


def tbody(*x, cls=None):
    return Tbody(*x, cls=cls)


def datatable(*, data: list[dict[str, Any]], columns: list[ColumnSpec]):
    return Div(
        Div(
            table(
                thead(
                    tablerow(*[th(k["header"]()) for k in columns]),
                ),
                tbody(
                    *[
                        tablerow(*[tablecell(c["cell"](item)) for c in columns])
                        for item in data
                    ]
                ),
            ),
            cls="rounded-md border",
        ),
        cls="space-y-4",
    )
