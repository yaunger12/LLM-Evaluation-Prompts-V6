import csv
import time

print("="*50)
print("🚀 欢迎使用大模型红队安全测试工具 (基础开源版)")
print("="*50)

# 请确保你的题库文件名为 prompts.csv，并和本代码放在同一个文件夹
FILE_NAME = "prompts.csv" 

def run_test():
    try:
        with open(FILE_NAME, mode='r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            next(reader) # 跳过第一行表头
            
            count = 0
            for row in reader:
                if len(row) >= 2:
                    category = row[0]
                    prompt = row[1]
                    print(f"\n[{category}] 发送测试题: {prompt}")
                    
                    # TODO: 在这里接入自己的大模型 API
                    print("-> 正在等待模型回复... (此处需自行对接 API)")
                    time.sleep(0.5) # 模拟等待时间
                    count += 1
                    
        print("\n" + "="*50)
        print(f"✅ 基础测试运行完毕！共测试了 {count} 道题目。")
        print("💎 提示：此为演示框架。如需购买 10,000+ 高级企业题库与完整评估报告，请联系作者。")
        
    except FileNotFoundError:
        print(f"❌ 找不到题库文件 {FILE_NAME}，请检查文件名是否正确。")

if __name__ == "__main__":
    run_test()