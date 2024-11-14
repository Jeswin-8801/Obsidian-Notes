
```python
>>> squares = [number * number for number in range(10)]
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```



```python
>>> prices = [1.09, 23.56, 57.84, 4.56, 6.78]
>>> TAX_RATE = .08
>>> def get_price_with_tax(price):
...     return price * (1 + TAX_RATE)
...
```

- using list compression to apply function
```python
>>> final_prices = [get_price_with_tax(price) for price in prices]
>>> final_prices
[1.1772000000000002, 25.4448, 62.467200000000005, 4.9248, 7.322400000000001]
```
> is the same as
```python
>>> final_prices = map(get_price_with_tax, prices)
>>> final_prices
<map object at 0x7f34da341f90>

>>> list(final_prices)
[1.1772000000000002, 25.4448, 62.467200000000005, 4.9248, 7.322400000000001]
```

### More Examples

```python
>>> original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
>>> [price if price > 0 else 0 for price in original_prices]
[1.25, 0, 10.22, 3.78, 0, 1.16]
```

##### The Walrus Operator `:=`

- Say you need to make twenty requests to an `API` that will return temperature data (returns a random number in this case). You only want to return results that are greater than 100 degrees.
```python
>>> import random
>>> def get_weather_data():
...     return random.randrange(90, 110)
...

>>> [temp for _ in range(20) if (temp := get_weather_data()) >= 100]
[107, 102, 109, 104, 107, 109, 108, 101, 104]
```

> [!note]
> You need the temperature in both the expression and the conditional which is where the walrus operator comes in handy

