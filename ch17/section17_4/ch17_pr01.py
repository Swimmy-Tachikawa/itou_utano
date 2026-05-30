"""ch17_pr01.py
次のプログラムの出力はA〜Dのどれでしょうか。
口頭で答えてみましょう。

A. こんばんは
　　こんにちは

B. こんにちは

C. こんばんは

D. こんにちは
　　こんばんは
"""

import asyncio

async def greet1():
    await asyncio.sleep(2)
    print("こんばんは")

async def greet2():
    await asyncio.sleep(1)
    print("こんにちは")

async def main():
    t1 = asyncio.create_task(greet1())
    t2 = asyncio.create_task(greet2())
    await t1
    await t2

asyncio.run(main())
