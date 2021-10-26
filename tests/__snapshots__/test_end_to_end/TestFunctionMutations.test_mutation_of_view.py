import datetime
from pathlib import *
from lineapy.data.types import *
from lineapy.utils import get_new_id

source_1 = SourceCode(
    code="""import lineapy
x = {}
y = {}
x[\'y\'] = y
y[\'a\'] = 1

lineapy.save(x, \'x\')
""",
    location=PosixPath("[source file path]"),
)
call_1 = CallNode(
    source_location=SourceLocation(
        lineno=2,
        col_offset=4,
        end_lineno=2,
        end_col_offset=6,
        source_code=source_1.id,
    ),
    function_id=LookupNode(
        name="__build_dict__",
    ).id,
)
call_2 = CallNode(
    source_location=SourceLocation(
        lineno=3,
        col_offset=4,
        end_lineno=3,
        end_col_offset=6,
        source_code=source_1.id,
    ),
    function_id=LookupNode(
        name="__build_dict__",
    ).id,
)
call_4 = CallNode(
    source_location=SourceLocation(
        lineno=5,
        col_offset=0,
        end_lineno=5,
        end_col_offset=10,
        source_code=source_1.id,
    ),
    function_id=LookupNode(
        name="setitem",
    ).id,
    positional_args=[
        call_2.id,
        LiteralNode(
            source_location=SourceLocation(
                lineno=5,
                col_offset=2,
                end_lineno=5,
                end_col_offset=5,
                source_code=source_1.id,
            ),
            value="a",
        ).id,
        LiteralNode(
            source_location=SourceLocation(
                lineno=5,
                col_offset=9,
                end_lineno=5,
                end_col_offset=10,
                source_code=source_1.id,
            ),
            value=1,
        ).id,
    ],
)
mutate_2 = MutateNode(
    source_id=call_2.id,
    call_id=call_4.id,
)
mutate_4 = MutateNode(
    source_id=MutateNode(
        source_id=MutateNode(
            source_id=call_1.id,
            call_id=CallNode(
                source_location=SourceLocation(
                    lineno=4,
                    col_offset=0,
                    end_lineno=4,
                    end_col_offset=10,
                    source_code=source_1.id,
                ),
                function_id=LookupNode(
                    name="setitem",
                ).id,
                positional_args=[
                    call_1.id,
                    LiteralNode(
                        source_location=SourceLocation(
                            lineno=4,
                            col_offset=2,
                            end_lineno=4,
                            end_col_offset=5,
                            source_code=source_1.id,
                        ),
                        value="y",
                    ).id,
                    call_2.id,
                ],
            ).id,
        ).id,
        call_id=call_4.id,
    ).id,
    call_id=call_4.id,
)
