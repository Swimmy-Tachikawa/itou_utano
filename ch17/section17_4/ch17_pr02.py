"""ch17_pr02.py
次のプログラムはtask1とtask2が順番に実行されるため、両方の処理が完了するまでに約5秒かかります。
プログラムを修正し、約3秒でどちらの処理も完了するようにしてください。
"""

import asyncio

async def task1():
    print("task1開始")
    await asyncio.sleep(3)
    print("task1終了")

async def task2():
    print("task2開始")
    await asyncio.sleep(2)
    print("task2終了")

async def main():
    await task1()
    await task2()

asyncio.run(main())
