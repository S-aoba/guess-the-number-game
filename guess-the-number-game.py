import random

while True:
    try:
        # ユーザーに最小値と最大値を入力してもらう
        # 数値以外の入力の場合は、ValueErrorを返して、再度入力させる
        minNumber_str = input("最小値を入力してください: ")
        maxNumber_str = input("最大値を入力してください: ")

        minNumber = int(minNumber_str)
        maxNumber = int(maxNumber_str)

        # 最小値が最大値よりも大きかった場合、再度入力してもらう
        if maxNumber < minNumber:
            while maxNumber < minNumber:
                print("最小値が最大値よりも大きいので、再度入力し直してください")
                minNumber = input("最小値を入力してください: ")
                maxNumber = input("最大値を入力してください: ")
        break
    except ValueError:
        print("数値を入力してください")

# ユーザーが入力した最小値と最大値の範囲内で乱数を生成する
random_number = random.randint(minNumber, maxNumber)
answer_count = 3
while True:
    print("生成された数値を予測して当ててみましょう。 あと ", answer_count, "回挑戦できます")
    user_number_str = input("数値を入力してください: ")

    user_number = int(user_number_str)

    if(random_number == user_number):
        print("おめでとうございます！ 生成された数値: ", random_number, "あなたが選んだ数値: ", user_number)
        break
    elif(answer_count == 1):
        break
    print("残念。再度予想してみてね！")
    answer_count -= 1

print("また挑戦してみてね！")