'''Includes String Templates for generating ASM code'''
from string import Template

tpl_start_text = """
    .text
main:
"""

tpl_start_data = """
    .data
"""

tpl_suma = Template("""

""")

tpl_resolve_var = Template("""
    lw  $$a0    $label
""")

tpl_assignment = Template("""
    sw  $$a0    $label
"""
)

# Imprimir enteros
tpl_printint = """
    li  $$v0 1
    lw  $$a0 $val
    syscall
"""

tpl_end = """
    li $v0  10
    syscall
"""
