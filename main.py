from collections import OrderedDict

def analyze_text(input_str):
    """统计字母字符频率，返回按频率降序排列的有序字典（匹配测试的字典类型要求）"""
    char_counts = {}
    # 1. 过滤非字母+统一大小写+统计频率
    for char in input_str:
        if not char.isalpha():
            continue
        lower_char = char.lower()
        char_counts[lower_char] = char_counts.get(lower_char, 0) + 1

    # 2. 按频率降序排序（频率相同按字符ASCII升序），构造有序字典
    # 有序字典既满足"字典类型"要求，又保证排序正确
    sorted_items = sorted(char_counts.items(), key=lambda x: (-x[1], x[0]))
    return OrderedDict(sorted_items)


if __name__ == "__main__":
    # 严格匹配测试要求的输出文案，无多余/缺失内容
    print("文本字符频率分析器")
    print("提示: 尝试输入中英文文章片段")
    user_input = input("请输入一段文本：")

    if not user_input:
        print("输入的字符串为空，无法分析。")
    else:
        result = analyze_text(user_input)
        print("字符频率降序排列：")
        # 遍历有序字典，按排序后的顺序打印
        for char, count in result.items():
            print(f"'{char}': {count}次")
