"""ch17_ex02.py
ロボットを作る以下のプログラムがあります。
現在はロボットの体・頭が完成する前に"ロボット完成！"と表示されてしまいます。
プログラムを修正し、体と頭が完成してから"ロボット完成！"が表示されるようにしてください。
ただし、実行から6秒以内に完成させるようにしてください。
"""

import asyncio

async def build_head():
    print("ロボットの頭を作っています")
    await asyncio.sleep(3)
    print("頭が完成しました")

async def build_body():
    print("ロボットの体を作っています")
    await asyncio.sleep(5)
    print("体が完成しました")

async def main():
    asyncio.create_task(build_head())
    asyncio.create_task(build_body())
    print("ロボット完成！")

asyncio.run(main())
