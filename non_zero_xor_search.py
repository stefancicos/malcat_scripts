import malcat
from malcat import Instruction

for fn in analysis.fns:
	for basic_block in analysis.cfg[fn.start : fn.end]:
		if basic_block.code:
			for insn in analysis.asm[basic_block.start : basic_block.end]:
				if insn.type == Instruction.Type.XOR:
					address = hex(analysis.a2v(insn.address))
					print(str(address)+" : "+str(insn))
					analysis.comments[insn.address] = "Non Zero XOR"
