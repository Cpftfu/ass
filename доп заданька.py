import asyncio

# функция намбер адин
async def square_shit (number):
    print(f'начало вычисления квадрата для численьки {number}')
    await asyncio.sleep(2) # тут у нас типа задержка (слава богу не в менструальном цикле)
    square = number ** 2
    print(f'Квадрат числа {number} равен {square}')
    return square

# функция намбер два
async def cube_shit (number):
    print(f'Начало вычисления куба для числа {number}')
    await asyncio.sleep(2)
    cube = number ** 3
    print(f'куб числа {number} равен: {cube}')
    return cube

# функция намбер три
async def jopa_operations():
    sq_result = await square_shit(2)
    cube_result = await cube_shit(sq_result)
    all = sq_result + cube_result
    print(f'cумма квадрата и куба равна^ {all}')

asyncio.run(jopa_operations())