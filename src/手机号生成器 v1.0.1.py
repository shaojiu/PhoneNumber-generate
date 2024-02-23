import csv

def generate_numbers(three, two, total):
    start = 0
    numbers = []
    for i in range(total):
        middle_six = str(start).zfill(6)
        full_number = three + middle_six + two
        print(full_number)
        numbers.append(full_number)
        start += 1
        if start > 999999:
            print("已达到中间手机号的最大可能值。")
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

def generate_and_save_numbers(three, two, total, format_type):
    numbers = generate_numbers(three, two, total)
    if format_type == 'CSV':
        save_numbers_to_csv(numbers)
        print(f"生成的数字已保存到 '{total} 条记录的 'Phone_numbers.csv' 文件中。")
    elif format_type == 'VCF':
        save_numbers_to_vcf(numbers)
        print(f"生成的数字已保存到 '{total} 条记录的 'Phone_numbers.vcf' 文件中。")
    else:
        print("未知的文件格式，请选择CSV或VCF。")

if __name__ == "__main__":
    print("手机号生成器 v1.0.1 Created：2024.2.23 Update：2024.2.24")
    print("GitHub开源项目：https://github.com/shaojiu/PhoneNumber-generate")
    three = input("请输入已知的前三位手机号：")
    two = input("请输入已知的后两位手机号：")
    if len(three) != 3 or not three.isdigit() or len(two) != 2 or not two.isdigit():
        print("输入有误，请确保前三位是三个数字，后两位是两个数字。")
    else:
        total = input("请输入需要生成的手机号数量：")
        if total.isdigit():
            total = int(total)
            format_type = input("请输入保存格式（CSV/VCF）：").upper()
            generate_and_save_numbers(three, two, total, format_type)
        else:
            print("请输入有效的数字量。")