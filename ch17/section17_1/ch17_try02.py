"""ch17_try02.py
コードを実行して動作を確認してください。
"""

import asyncio

async def order_pizza():
    print("ピザを注文しました")
    await asyncio.sleep(3)
    print("ピザが届いた！")

async def do_homework():
    print("宿題開始！")
    for i in range(1, 4):
        print(f"宿題 {i} ページ目")
        await asyncio.sleep(1)

async def main():
    pizza_task = asyncio.create_task(order_pizza())
    homework_task = asyncio.create_task(do_homework())
    await pizza_task
    await homework_task

asyncio.run(main())
