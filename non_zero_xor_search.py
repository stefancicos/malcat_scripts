"""
name: Non Zero XOR Search
category: pe
author: stefancicos
icon: wxART_DISASM

Searches for non-zero xor instructions and prints them to the console, while also adding a comment.

https://github.com/stefancicos/malcat_scripts

"""

import malcat
from malcat import Instruction

for fn in analysis.fns:
	for basic_block in analysis.cfg[fn.start : fn.end]:
		if basic_block.code:
			for insn in basic_block:
				if insn.type == Instruction.Type.XOR:
					gui.print(f"[rva]{insn.address:x}[/rva]: "+str(insn).replace("[","\[")+" ", format=True) # TODO: remove +" " after the bug is fixed
					analysis.comments[insn.address] = "Non Zero XOR"
