import csv
def generate_numbers(prefix, suffix, total, middle_digits_length=6):
    start = 0
    numbers = []
    for i in range(total):
        middle = str(start).zfill(middle_digits_length)
        full_number = prefix + middle + suffix
        print(full_number)
        numbers.append(full_number)
        start += 1
        if start > 10 ** middle_digits_length - 1:
            print("已达到中间号码的最大可能值。")
            break
    return numbers
def save_numbers_to_csv(numbers, filename='Phone_numbers.csv'):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['PhoneNumber'])
        for number in numbers:
            writer.writerow([number])


def save_numbers_to_vcf(numbers, filename='Phone_numbers.vcf'):
    with open(filename, 'w') as file:
        for number in numbers:
            file.write("BEGIN:VCARD\n")
            file.write("VERSION:3.0\n")
            file.write(f"FN:{number}\n")
            file.write(f"TEL;CELL:{number}\n")
            file.write("END:VCARD\n")


def generate_and_save_numbers(prefix, suffix, total, format_type):
    middle_digits_length = 11 - len(prefix) - len(suffix)
    numbers = generate_numbers(prefix, suffix, total, middle_digits_length)
    if format_type == 'CSV':
        save_numbers_to_csv(numbers)
        print(f"生成的数字已保存到 '{total} 条记录的 'Phone_numbers.csv' 文件中。")
    elif format_type == 'VCF':
        save_numbers_to_vcf(numbers)
        print(f"生成的数字已保存到 '{total} 条记录的 'Phone_numbers.vcf' 文件中。")
    else:
        print("未知的文件格式，请选择CSV或VCF。")


if __name__ == "__main__":
    print("手机号生成器 v1.1.0 Created：2024.2.23 Update：2024.2.27")
    print("他现在支持输入前几位+后几位来生成中间的几位了，比如说前5后5生成中间的一位数。")
    print("GitHub开源项目：https://github.com/shaojiu/PhoneNumber-generate")
    prefix = input("请输入已知的前几位手机号：")
    suffix = input("请输入已知的后几位手机号：")
    if not prefix.isdigit() or not suffix.isdigit() or len(prefix) + len(suffix) >= 11:
        print("输入有误，请确保前缀和后缀是数字，并且总长度小于11。")
    else:
        total = input("请输入需要生成的手机号数量：")
        if total.isdigit():
            total = int(total)
            format_type = input("请输入保存格式（CSV/VCF）：").upper()
            generate_and_save_numbers(prefix, suffix, total, format_type)
        else:
            print("请输入有效的数字量。")