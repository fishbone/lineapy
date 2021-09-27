from lineapy import SessionType, Tracer, Variable, ExecutionMode

lineapy_tracer = Tracer(SessionType.SCRIPT, "[source file path]", ExecutionMode.MEMORY)
lineapy_tracer.call(
    function_name="not_",
    syntax_dictionary={
        "lineno": 1,
        "col_offset": 0,
        "end_lineno": 1,
        "end_col_offset": 10,
    },
    arguments=[
        lineapy_tracer.call(
            function_name="contains",
            syntax_dictionary={
                "lineno": 1,
                "col_offset": 0,
                "end_lineno": 1,
                "end_col_offset": 10,
            },
            arguments=[Variable("b"), Variable("a")],
            keyword_arguments=[],
        )
    ],
    keyword_arguments=[],
)
lineapy_tracer.exit()